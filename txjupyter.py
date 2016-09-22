def start():
    from tornado.platform.twisted import install
    return install()

def klein(reactor, description):
    from twisted.web.server import Site
    from twisted.internet import endpoints
    from klein import route, resource
    ep = endpoints.serverFromString(reactor, description)
    s = Site(resource())
    ep.listen(Site(resource()))
