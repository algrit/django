from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponseRedirect


def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('done')
        else:
            form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form})


def feedback_update(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedbacks/done')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/index.html', {'form': form})


def done(request):
    return render(request, 'feedback/done.html')
