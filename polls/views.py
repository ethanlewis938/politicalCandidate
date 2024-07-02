from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    """
    Display the latest five questions in the poll application.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        The rendered poll page with the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def vote(request, question_id):
    """
    Process a vote for a particular question.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.
    question_id : int
        The ID of the question being voted on.

    Returns
    -------
    HttpResponseRedirect
        Redirects to the results page after a successful vote.
    HttpResponse
        The rendered voting form page with an error message if no choice was selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        }) 
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )

def detail(request, question_id):
    """
    Display the details of a particular question.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.
    question_id : int
        The ID of the question to display.

    Returns
    -------
    HttpResponse
        The rendered detail page for the specified question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Display the results of a particular question.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.
    question_id : int
        The ID of the question for which to display results.

    Returns
    -------
    HttpResponse
        The rendered results page for the specified question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})