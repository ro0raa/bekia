from django.contrib import admin
from .models import Advertisement,Images,AdvTypes


admin.site.register(AdvTypes)
admin.site.register(Advertisement)
admin.site.register(Images)
# Register your models here.
