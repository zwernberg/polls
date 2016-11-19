from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse

from polls.models import Question
from polls.forms import QuestionForm, ChoiceFormSet

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class CreateView(generic.CreateView):
    model = Question
    template_name = 'polls/create.html'
    #fields = ['question_text',]
    form_class = QuestionForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet()
        
        return self.render_to_response(self.get_context_data(form=form, choice_form=choice_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet(self.request.POST)
        if (form.is_valid() and choice_form.is_valid()):
            return self.form_valid(form,choice_form)
        else:
            return self.form_invalid(form,choice_form)
    
    def form_valid(self, form, choice_form):
        self.object = form.save()
        choice_form.instance = self.object
        choice_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form, choice_form=choice_form)
        )

    def get_success_url(self):
        return reverse('polls:detail',args=(self.object.id,))

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_mesage': "You didn't select a valid choice.", 
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))