convert model to dict in python :
model_data= Product.objects.all().order_by("?").first()
data ={}
if modal_data:
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content


In above we have converted modal data to python dictionary

The above method can be simplified as 
model_data= Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         data = model_to_dict(model_data,fields=['id','title','price'])
#     return Response(data)

here model_to_dict()is a inbuily function which convert model data to python dictionary
and it is imported from  
from django.forms.models import model_to_dict

2:23