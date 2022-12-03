from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question,Choice
# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "latest_question_list"
    template_name = "polls/index.html"
    def get_queryset(self):        
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = "polls\details.html"
    model = Question
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte==timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

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