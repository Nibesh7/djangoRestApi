# ListModelMixin -> It is for listing all the item
                 -> It doesn't care about the lookup_field

# RetrieveModelMixin -> It is for listing the detail of single item
                     -> It reqires lookup_field
                     -> lookup_field = 'pk'
                     -> By default lookup_field is 'pk'