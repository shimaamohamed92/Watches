
from gowatches.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    UserViewSet,
)
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
# router.register(r'all', UserViewSet)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('user/<int:pk>/', UserViewSet.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)