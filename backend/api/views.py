from itertools import product
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
#================================
# Django Rest Framework view
#================================

#Using Searializers
# @api_view(["GET"]) #-> Decorators
# def api_home(request,*args,**kwargs):
#     """DRF API View"""
#     instance= Product.objects.all().order_by("?").first()
#     data ={}
#     if instance:
#         data = ProductSerializers(instance).data
#     return Response(data)

@api_view(["POST"]) #-> Decorators
def api_home(request,*args,**kwargs):
    """DRF API View"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
#without using searilizers

# @api_view(["GET"]) #-> Decorators
# def api_home(request,*args,**kwargs):
#     """DRF API View"""
#     model_data= Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         data = model_to_dict(model_data,fields=['id','title','price'])
#     return Response(data)

#end without using searilizers

#============================
# END OF REST FRAMEWORK
#============================



#====================
#       This is django view
#=======================
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         #model instance to dict this is manual way
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
        
#         #shortcut to model instance to dict
#         data = model_to_dict(model_data,fields=['id','price'])
#     return JsonResponse(data)

# def api_home(request,*args,**kwargs):
#     #request -> instance of ->HttpRequest class from ->django
#     #print(dir(request))
#     #request.body 
#     print(request.GET)
#     body = request.body # byte string of json data
#     data ={}
#     try:
#         data = json.loads(body) #string of JSON data -> dict 
#     except:
#         pass
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     # print(data.keys())
#     # print(request.headers)
#     print(data)
#     #converting the json byer string to dictionary
#     return JsonResponse({"message":"From django view"})