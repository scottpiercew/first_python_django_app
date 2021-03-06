from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from .models import Choice, Question


def index(request):
    # displays the most recent five questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # loads the template called polls/index.html

#this uses the helper function get_object_or_404() to repace the commented out code below
def detail(request, question_id):
    #     #similar to a JavaScript switch statement, a 404 error will be raised if the requested ID doesn't exist
    #     try:
    #         question = Question.objects.get(pk=question_id)
    #     except Question.DoesNotExist:
    #         raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
#redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
#returns an HttpResponseRedirect after successfully dealing with POST data.
#prevents data from being posted twice if a user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
