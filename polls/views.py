from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.QuestionText for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    response = f"you're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"You're voting on quesion {question_id}")