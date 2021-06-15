from rest_framework.viewsets import ModelViewSet
from .serializers import DirectorySerializer, DirectoryElementSerializer
from .models import Directory


class DirectoryView(ModelViewSet):

    """Данная вьюшка подерживает все базовые запросы: GET, PUT, PATCH, DELETE, OPTIONS"""

    serializer_class = DirectorySerializer
    queryset = Directory.objects.all()
    filter_fields = ('date', )

    def filter_queryset(self, queryset):
        date = self.request.query_params.get('date')
        version = self.request.query_params.get('version')
        name = self.request.query_params.get('name')
        if name and version:
            self.serializer_class = DirectoryElementSerializer
            queryset = queryset.filter(name=name, version=version).first().directoryelement_set.all()
        if date:
            queryset = queryset.filter(date__gte=date)
        return queryset
