from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet,
                    get_confirmation_code, get_token)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews', ReviewViewSet, basename='Review'
)
v1_router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)

urlpatterns_auth = [
    path('email/', get_confirmation_code, name='confirmation'),
    path('token/', get_token, name='token'),
]

urlpatterns = [
    path('v1/auth/', include(urlpatterns_auth)),
    path('v1/', include(v1_router.urls)),
]
