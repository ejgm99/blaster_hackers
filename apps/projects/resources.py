from .models import Component, Project
from import_export import resources

class ComponentResource(resources.ModelResource):
    class Meta:
        model = Component
        skip_unchanged = True


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        skip_unchanged = True
