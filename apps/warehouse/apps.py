from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WarehouseConfig(AppConfig):
    name = 'apps.warehouse'
    verbose_name = _('warehouse')
