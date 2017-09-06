//
// CFC URL
//
//var cfc_url = "wss://fabric.crossbario.com/ws";
var cfc_url = "ws://localhost:9000/ws";


// once we have successfully logged in to CFC, run this code:

function main(session) {
   console.log('PUT YOUR CFC USER CODE HERE!');

   session.call('crossbarfabriccenter.system.get_status').then(
      function (res) {
         console.log(res);
      },
      function (err) {
         console.log(err);
      }
   );
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

      // now run our actual user main code ..
      main(session);
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
         if (details.reason == 'fabric.auth-failed.new-user-auth-code-sent') {
            localStorage.setItem('cfc.activation_status', 'sent');
         } else {
            console.log('WARN: getting here is unexpected ..');
            console.log(details.reason);
            console.log(details.message);
         }
         location.reload()
      }

      connection.open();
   }
}
