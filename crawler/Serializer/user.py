from rest_framework import serializers
from crawler.models.Users import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        field = ['email', 'name', 'created_at', 'updated_at']