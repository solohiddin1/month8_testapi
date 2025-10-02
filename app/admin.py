from django.contrib import admin
from .models import Tovar, Xodim, Zakaz , Mijoz

# Register your models here.


admin.site.register(Xodim)
admin.site.register(Mijoz)
admin.site.register(Zakaz)
# admin.site.register(Statistics)
admin.site.register(Tovar)
