# marketplace/apps.py
from django.apps import AppConfig

class MarketplaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace'

class MarketplaceConfig(AppConfig):
    name = 'marketplace'

    def ready(self):
        import marketplace.signals