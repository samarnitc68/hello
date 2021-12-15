from django.contrib import admin
from home.models import Author, Blog, Entry, department_detals, employee_details

admin.site.register(employee_details)
admin.site.register(department_detals)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)

# Register your models here.
