from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import WatchesAPI, VariantAPI, variant_detail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
     path('watches/', WatchesAPI.as_view()),
     path('variants/', VariantAPI.as_view()), 
     path('variant/<int:pk>/', variant_detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)