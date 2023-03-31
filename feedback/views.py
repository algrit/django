from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponseRedirect


def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            new_item = Feedback(
                name=request.POST['name'],
                rating=request.POST['rating'],
                comment=request.POST['comment'],
            )
            new_item.save()
            return HttpResponseRedirect('done')
        else:
            form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form})


def done(request):
    return render(request, 'feedback/done.html')