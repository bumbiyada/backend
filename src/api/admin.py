from django.contrib import admin
from .models import ListAll
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(ListAll)
class ListAllAdmin(ImportExportModelAdmin):
    list_display = ('Foiv', 'Document_type', 'Document_number', 'Document_init_data',
                    'Stage_name', 'Stage_data', 'Stage_user', 'Is_aborted', 'Is_done', 'Marked_on_delete')
    pass


#.site.register(ListAll, ListAllAdmin)
