from django.contrib import admin
from .models import Tovar, Xodim, Zakaz , Mijoz,ZakazItem

# Register your models here.


admin.site.register(Xodim)
admin.site.register(Mijoz)
admin.site.register(Zakaz)
admin.site.register(Tovar)
admin.site.register(ZakazItem)
