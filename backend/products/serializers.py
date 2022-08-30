from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk',
    )
    email = serializers.EmailField(write_only=True)
    
    #Custom Validation Method 2
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'pk',
            'edit_url',
            'email',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    #=================================================
    #               Custom Validation 
    #=================================================
    #Method 1:
    # def validate_title(self,value): #validate_field_name
    #     qs = Product.objects.filter(title__iexact=value)
    #     #iexact is for case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    #Unpacking email form validation 
    # Removed because it van be done in create method in view
    # def create(self,validated_data):
    #     print('validated data =', validated_data)
    #     email = validated_data.pop('email')
    #     print('validate data after pop', validated_data)
    #     obj = super().create(validated_data)
    #     print(email,obj)
    #     return obj

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk}, request = request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()