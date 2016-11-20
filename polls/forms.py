from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from polls.models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

ChoiceFormSet = inlineformset_factory(Question,Choice,form=ChoiceForm, fields=('choice_text',), extra=0 ,min_num=1, max_num=5 )

