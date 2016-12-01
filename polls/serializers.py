from rest_framework import serializers
from polls.models import Question, Choice
        
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'id', 'choice_text', 'votes')
        read_only_fields = ('votes',)
        
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ('url', 'slugfield', 'question_text', 'choices',)
        read_only_fields = ('slugfield',)
        lookup_field = 'slugfield'
        extra_kwargs = {
            'url': {'lookup_field': 'slugfield'}
        }

        
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        
        return question