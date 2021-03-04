from question.models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    """
    Questions model fields serializer
    """
    class Meta:
        model = Question
        depth = 1
        fields = ('id', 'name', 'options', 'correct_option', 'quiz', 'points')