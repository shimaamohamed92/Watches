from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse
from rest_framework import mixins
from .serializers import WatchesSerializer, TrackSerializer, vairiantSerializer
from .models import Watches, Varient
from gowatches.users.models import User
from rest_framework import generics
from rest_framework.response import Response


class WatchesAPI(generics.ListAPIView,):
    queryset = Watches.objects.all()
    serializer_class = WatchesSerializer


class VariantAPI(generics.ListAPIView, mixins.CreateModelMixin,):
    queryset = Varient.objects.all()
    serializer_class = vairiantSerializer


    def post(self, request):
        # nationalid = request.data.get("nantional_id")
        # variant, created  = Varient.objects.get_or_create(nantional_id=nationalid)
        

        serializer = vairiantSerializer(variant)

        return Response(serializer.data)


class variant_detail(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Varient.objects.all()
    serializer_class = vairiantSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request,pk=None,format=None):
        variant=self.kwargs["pk"]
        variant_obj = Varient.objects.get(id=variant)
        serializer=vairiantSerializer(variant,data=request.data)
        user = User.objects.get(id=self.request.user.id) 
        user.variant_list.add(variant)
        user.save()
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

