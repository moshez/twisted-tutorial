from __future__ import print_function
from klein import route, resource
from twisted.web.server import Site
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor, defer
from twisted.python import log

lport, endpoint = [], TCP4ServerEndpoint(reactor, 8080)
def listen():
    if lport:
        port = lport.pop()
        d = port.stopListening()
    else:
        d = defer.succeed(None)
    def actuallyListen(dummy):
        s = Site(resource())
        d = endpoint.listen(Site(resource()))
        d.addCallback(lport.append)
    d.addCallback(actuallyListen)

@route('/')
def home(request):
    return 'Hello, world!'
listen()

def addRoute():
    @route('/lala')
    def thingy(request):
        return 'lolo'
    listen()

reactor.callLater(2, addRoute)
reactor.run()
