from django.contrib import admin
from .models import Scene,report,module
# Register your models here.
class SceneAdmin(admin.ModelAdmin):
    list_display = ['name','module_list']
admin.site.register(Scene,SceneAdmin)
admin.site.register(report)
admin.site.register(module)