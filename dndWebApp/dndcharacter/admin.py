from django.contrib import admin
from dndcharacter.models import Characters
from dndcharacter.models import Observations

# Register your models here.
admin.site.register(Characters)
admin.site.register(Observations)