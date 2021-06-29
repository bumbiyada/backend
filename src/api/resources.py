from import_export import resources
from .models import ListAll


class ListAllResource(resources.ModelResource):
    class Meta:
        model = ListAll
