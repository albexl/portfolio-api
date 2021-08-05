from django.contrib import admin
from django.db import models

from project.models import ProjectInfo


def CustomModelAdmin(model):
    return type('SubClass' + model.__name__,
                (admin.ModelAdmin,
                 ),
                {'list_display': [x.name for x in model._meta.fields],
                    'list_select_related': [x.name for x in model._meta.fields if isinstance(x,
                                                                                             (models.ManyToOneRel,
                                                                                              models.ForeignKey,
                                                                                              models.OneToOneField,
                                                                                              ))],
                 'search_fields': ['id'],
                 'list_display_links': ['id'],
                 })


admin.site.register(ProjectInfo, CustomModelAdmin(ProjectInfo))
