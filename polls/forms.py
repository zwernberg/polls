from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from polls.models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

ChoiceFormSet = inlineformset_factory(Question,Choice,form=ChoiceForm, fields=('choice_text',), extra=3 )

