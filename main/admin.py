from django.contrib import admin
from main.models import Category,Director,Movie,Review,Tag

# Register your models here.

admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Tag)