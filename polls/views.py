from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list}        
    return render(request,'polls\index.html',context)

def detail(request,question_id):
    try:
        q = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exist")
    return render(request, 'polls\details.html',{'question':q})    

def results(request, question_id):
    response = f"you're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"You're voting on quesion {question_id}")