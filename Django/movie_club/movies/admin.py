from django.contrib import admin

# Register your models here.
from .models import movies_list,movies
class moviesAdmin(admin.ModelAdmin):
	list_display=["name","rating"]
	search_fields=["name","rating","type"]
admin.site.register(movies_list)
admin.site.register(movies,moviesAdmin)