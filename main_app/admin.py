from django.contrib import admin
from .models import Owl, Feeding, Toy

# Register your models here.
admin.site.register(Owl)
admin.site.register(Feeding)
admin.site.register(Toy)