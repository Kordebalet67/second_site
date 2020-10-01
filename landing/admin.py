from django.contrib import admin
from .models import *

# Register your models here.


class Subscriber1Admin (admin.ModelAdmin):
    list_display = [field.name for field in Subscriber1._meta.fields]  # ["surname", "first_name"]
    search_fields = ["first_name", "surname", "birth_date"]

    class Meta:
        model = Subscriber1


admin.site.register(Subscriber)
admin.site.register(Subscriber1, Subscriber1Admin)
