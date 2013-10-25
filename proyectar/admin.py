from django.contrib import admin
from proyectar.models import Presentacion, Slides

class SlidesInline(admin.StackedInline):
	model = Slides

class PresentacionAdmin(admin.ModelAdmin):
	list_display = ['nombre','autor','descripcion']
	search_fields = ['nombre']
	list_filter = ['autor']
	inlines = [SlidesInline]


admin.site.register(Presentacion,PresentacionAdmin)
admin.site.register(Slides)