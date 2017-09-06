//
// CFC URL
//
var cfc_url = "wss://fabric.crossbario.com/ws";
//var cfc_url = "ws://localhost:9000/ws";


// once we have successfully logged in to CFC, run this code on
// the user management realm
function main(session) {
   console.log('PUT YOUR CFC USER CODE HERE!');

   var nodes;

   session.call('crossbarfabriccenter.mrealm.get_nodes').then(
      function (nodes) {
         nodes = nodes;
         console.log(nodes);
         for (var i = 0; i < nodes.length; ++i) {
            var node_id = nodes[i];
            session.call('crossbarfabriccenter.mrealm.get_node', [node_id]).then(
               function (node) {
                  console.log(node);
               },
               function (err) {
                  console.log(err);
               }
            );
         }
      },
      function (err) {
         console.log(err);
      }
   )
}


//
// the stuff below is a poor man's user register/activate/login flow.
// obviously, in a production UI, you want sth better than prompt() ;)
//

// private key for WAMP-cryptosign (auto-generated if there is none)
var pkey = autobahn.auth_cryptosign.load_private_key('cfc.key');

// user email address
var email_address = localStorage.getItem('cfc.email');
if (!email_address) {
   email_address = prompt("Please enter your email address");
   localStorage.setItem('cfc.email', email_address);
   location.reload();
}

// activation token and status
var activation_code = localStorage.getItem('cfc.activation_code');
var activation_status = localStorage.getItem('cfc.activation_status');

// the management realm the user wants to ultimately connect to
var management_realm = localStorage.getItem('cfc.management_realm');


if (activation_code) {

   var config = {
      url: cfc_url,

      // global users realm
      realm: null,

      // user email
      authid: email_address,

      // user private key
      pkey: pkey,

      // enforce re-sending of new activation code
      request_new_activation_code: false
   }

   if (activation_status === 'activated') {
      console.log('already activated!')

      if (!management_realm) {
         management_realm = prompt('Please enter your management realm');
         localStorage.setItem('cfc.management_realm', management_realm);
      } else {
         config.realm = management_realm;
      }
   } else {
      console.log('ok, got key, email and activation code .. now activate');
      config.activation_code = activation_code;
   }

   var connection = autobahn.auth_cryptosign.create_connection(config);

   connection.onopen = function (session, details) {
      console.log("Connected to CFC:", session.id, details);

      if (activation_status !== 'activated') {
         activation_status = 'activated';
         localStorage.setItem('cfc.activation_status', activation_status);
      }

      if (session.realm === 'com.crossbario.fabric') {
         session.call('crossbarfabriccenter.system.get_status').then(
            function (res) {
               console.log(res);
            },
            function (err) {
               console.log(err);
            }
         );
         session.leave();
         location.reload()
      } else {
         // now run our actual user main code ..
         main(session);
      }
   }

   connection.onclose = function (reason, details) {
      console.log(details.reason);
      console.log(details.message);
   }

   connection.open();

} else {
   // user is new ..

   if (activation_status === 'sent') {
      // .. but supposed to have received an activation code already
      activation_code = prompt("Please enter your activation code");
      localStorage.setItem('cfc.activation_code', activation_code);
      location.reload();

   } else {
      // .. and needs an activation code, so request one by connecting to CFC
      var config = {
         url: cfc_url,

         // global users realm
         realm: null,

         // user email
         authid: email_address,

         // user private key
         pkey: pkey,

         // enforce re-sending of new activation code
         request_new_activation_code: false
      }

      var connection = autobahn.auth_cryptosign.create_connection(config);

      connection.onclose = function (reason, details) {
         if (details.reason == 'fabric.auth-failed.new-user-auth-code-sent' || details.reason == 'fabric.auth-failed.registered-user-auth-code-sent') {
            localStorage.setItem('cfc.activation_status', 'sent');
            location.reload();
         } else if (details.reason == 'fabric.auth-failed.pending-activation') {
            localStorage.setItem('cfc.activation_status', 'sent');
            console.log(details.message);
            console.log('hit reload when you got your activation code!');
         } else {
            console.log('WARN: getting here is unexpected ..');
            console.log(details.reason);
            console.log(details.message);

/*
    ERROR_AUTH_INVALID_PARAMETERS = u'fabric.auth-failed.invalid-parameters'
    ERROR_AUTH_INVALID_PARAMETERS_MSG = u'Invalid parameters in authentication: {}'

    ERROR_AUTH_PENDING_ACT = u'fabric.auth-failed.pending-activation'
    ERROR_AUTH_PENDING_ACT_MSG = u'There is a pending activation (from {} ago) - please check your email inbox, or request a new code'

    ERROR_AUTH_NO_PENDING_ACT = u'fabric.auth-failed.no-pending-activation'
    ERROR_AUTH_NO_PENDING_ACT_MSG = u'There is no (pending) activation for this user/pubkey, but an activation code was provided'

    ERROR_AUTH_INVALID_ACT_CODE = u'fabric.auth-failed.invalid-activation-code'
    ERROR_AUTH_INVALID_ACT_CODE_MSG = u'This activation code is invalid: {}'

    ERROR_AUTH_NODE_UNPAIRED = u'fabric.auth-failed.node-unpaired'
    ERROR_AUTH_NODE_UNPAIRED_MSG = u'This node is unpaired. Please pair the node with management realm first.'

    ERROR_AUTH_EMAIL_FAILURE = u'fabric.auth-failed.email-failure'

    ERROR_AUTH_NEW_USER = u'fabric.auth-failed.new-user-auth-code-sent'
    ERROR_AUTH_NEW_USER_MSG = u'We have sent an authentication code to {email}.'

    ERROR_AUTH_REGISTERED_USER = u'fabric.auth-failed.registered-user-auth-code-sent'
    ERROR_AUTH_REGISTERED_USER_MSG = u'We have sent an authentication code to {email}.'
 */
         }
      }

      connection.open();
   }
}
