from __future__ import absolute_import

from django.contrib import admin

from metatag import models as mm


class MetaAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'description', 'keywords')


admin.site.register(mm.URLMetatags, MetaAdmin)
