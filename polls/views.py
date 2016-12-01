from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response


from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

# Create your views here.
class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slugfield'

    
class ChoiceViewset(viewsets.ReadOnlyModelViewSet):

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
    @detail_route(methods=['post'])
    def vote(self, request, pk):
        choice = get_object_or_404(Choice,id=pk)
        choice.votes += 1
        choice.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
       
