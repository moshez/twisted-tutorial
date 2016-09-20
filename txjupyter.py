def start(description):
    from tornado.platform.twisted import install
    reactor = install()
    from twisted.web.server import Site
    from twisted.internet import endpoints
    from klein import route, resource
    ep = endpoints.serverFromString(reactor, description)
    s = Site(resource())
    ep.listen(Site(resource()))
    return reactor