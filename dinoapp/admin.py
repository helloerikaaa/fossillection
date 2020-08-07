from django.contrib import admin
from .models import Fossil, Meteor, Mineral, Rock

# Register your models here.
admin.site.register(Fossil)
admin.site.register(Meteor)
admin.site.register(Mineral)
admin.site.register(Rock)