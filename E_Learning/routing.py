from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostOriginValidator
from home.consumers import ChatConsumer


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)

    "websocket":  AuthMiddlewareStack(
            URLRouter([
                path(r'stufinf/chatroom/(?P<user1>[\w.@+-]+)/(?P<user2>[\w.@+-]+)/', ChatConsumer)
            ])
    )

})