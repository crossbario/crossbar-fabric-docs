###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Crossbar.io Technologies GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

from twisted.internet.defer import inlineCallbacks, returnValue

import client


@inlineCallbacks
def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    session.log.info('running main() ...')
    return_code = 0
    try:
        nodes = yield session.call(u'crossbarfabriccenter.get_nodes')
        for node_id in nodes:
            workers = yield session.call(u'crossbarfabriccenter.remote.get_workers', node_id)
            for worker_id in workers:
                worker = yield session.call(u'crossbarfabriccenter.remote.get_worker', node_id, worker_id)
                session.log.info('Node "{node_id}" / Worker "{worker_id}": {worker}', node_id=node_id, worker_id=worker_id, worker=worker)
    except:
        # something bad happened: investigate your side or pls file an issue;)
        return_code = -1
        session.log.failure()
    finally:
        # in any case, shutdown orderly
        session.leave()

    returnValue(return_code)


if __name__ == '__main__':
    client.run(main)
