instance= Product.objects.all().order_by("?").first()

data = ProductSerializers(instance).data

Here ProductSerializers(instance) make the class the instance and .data is the data that is coming through that instance