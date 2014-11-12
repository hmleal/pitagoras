from django.contrib import admin
from . import models


class PathWayAdmin(admin.ModelAdmin):
    filter_horizontal = ('gmms',)


class GmmAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.PathWay, PathWayAdmin)
admin.site.register(models.Gmm, GmmAdmin)
