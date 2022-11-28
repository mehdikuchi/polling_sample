from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list}        
    return render(request,'polls\index.html',context)

def detail(request,question_id):
    """ 
    try:
        q = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exist")
        """
    q = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls\details.html',{'question':q})    

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})
    # numvotes = question.choice_set.get(pk = question_id)
    # response = f"you're looking at the results of question {question_id} and the number of votes is {numvotes.votes}"
    # return HttpResponse(response)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except:
        return render(request,"polls/details.html",\
            {"question":question,"error_message":"You didn't select an option"})    
    selected_choice.votes+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
    # return HttpResponse(f"You're voting on quesion {question_id}")