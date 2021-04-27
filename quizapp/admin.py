from django.contrib import admin
from .models import Detail, EasyQuestion, HardQuestion

# Register your models here.
admin.site.register(Detail)
admin.site.register(EasyQuestion)
admin.site.register(HardQuestion)