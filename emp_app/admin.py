from django.contrib import admin

# Register your models here.
from .models import Bedroom,Kitchen,Hall,Handles,Doors,Bedroom_handles,Bedroom_doors,Hall_handles,Hall_doors,Checkout


admin.site.register(Kitchen)
admin.site.register(Bedroom)
admin.site.register(Hall)
admin.site.register(Handles)
admin.site.register(Doors)
admin.site.register(Bedroom_handles)
admin.site.register(Bedroom_doors)
admin.site.register(Hall_handles)
admin.site.register(Hall_doors)
admin.site.register(Checkout)
