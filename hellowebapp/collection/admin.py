from django.contrib import admin

from collection.models import SwimFace
# Register your models here.

class SwimFaceAdmin(admin.ModelAdmin):
	model = SwimFace
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(SwimFace, SwimFaceAdmin)