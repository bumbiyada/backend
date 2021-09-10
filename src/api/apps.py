from django.apps import AppConfig

from scheduler import updater


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'ABOBA_ABIBA'

    def ready(self):
        updater.start()
