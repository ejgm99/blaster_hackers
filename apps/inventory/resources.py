from .models import Item, Type
from import_export import resources

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        skip_unchanged = True
