from rest_framework import generics, mixins
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from api.permission import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixins
#or from django.http import Http404
from .serializers import ProductSerializer
# from api.authentication import TokenAuthentication

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
'''
    This is createAPIView With ListAPIView
'''
class ProductListCreateAPIView(StaffEditorPermissionMixins, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    # ]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.DjangoModelPermissions]

    #======================== Replaced By Mixins ===========================
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    def perform_create(self,serializer):
        email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

'''
    This is only CreateAPIView 
'''
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self,serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)

'''
    Not in use becase create view cand be modeified to used as listAPIView
'''
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class productUpdateAPIView(StaffEditorPermissionMixins,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class productDeleteAPIView(StaffEditorPermissionMixins,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # print('in delete')
    def perform_destroy(self, instance):
        print("perform delete",instance)
        return super().perform_destroy(instance)

'''

mixins.ListModelMixin -> provide the ability to use queryset
like queryset = Product.objects.all()

'''
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        #.list()-> is provided by ListModelMixin
        return self.list(request, *args, **kwargs)
        
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "workin in DRF create mixin"
        serializer.save(content=content)

@api_view(["GET","POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            #details view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
            #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
    if method == "POST":
        #create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)