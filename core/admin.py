from django.contrib import admin
from . import models


class PathWayAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    filter_horizontal = ('gmms',)


class GmmAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.PathWay, PathWayAdmin)
admin.site.register(models.Gmm, GmmAdmin)
