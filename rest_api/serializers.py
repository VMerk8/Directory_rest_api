from rest_framework import serializers
from .models import Directory, DirectoryElement


class DirectorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Directory
        fields = ['id', 'name', 'short_name', 'description', 'version', 'date']


class DirectoryElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = DirectoryElement
        fields = ['directory_id', 'element_code', 'element_value']
