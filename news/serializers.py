from rest_framework import serializers
from news import models as news_models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= news_models.News
        fields = ['id','title', 'content', 'date']