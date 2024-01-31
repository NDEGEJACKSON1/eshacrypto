from rest_framework_nested import routers

from posts.viewsets import PostViewSet
from user.viewsets import UserViewSet
from auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
)
from comment.viewsets import CommentViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")


# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #

router.register(r"user", UserViewSet, basename="user")

# ##################################################################### #
# ################### POST                       ###################### #
# ##################################################################### #

router.register(r"posts", PostViewSet, basename="posts")

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="posts")
posts_router.register(r"comment", CommentViewSet, basename="post-comment")


urlpatterns = [*router.urls, *posts_router.urls]
