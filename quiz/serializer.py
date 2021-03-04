from quiz.models import Quiz
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    """
    Quiz model fields serializer
    """
    class Meta:
        model = Quiz
        fileds = '__all__'
        exclude = ()


