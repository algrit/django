from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/index.html', {'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('done/')
#         else:
#             return render(request, 'feedback/index.html', {'form': form})
class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    success_url = '/done'

    def form_valid(self, form):
        form.save()
        return super(FeedbackView, self).form_valid(form)


# class FeedbackUpdateView(View):
#     def get(self, request, id_feedback):
#         feed_obj = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=feed_obj)
#         return render(request, 'feedback/index.html', {'form': form})
#
#     def post(self, request, id_feedback):
#         feed_obj = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feed_obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#         else:
#             return render(request, 'feedback/index.html', {'form': form})
class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    success_url = '/done'



class ListFeedback(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gte=3)
        return filter_qs


# class OneFeedback(TemplateView):
#     template_name = 'feedback/onefeedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedback = Feedback.objects.get(id=context['id_feedback'])
#         context['feedback'] = feedback
#         return context
class DetailFeedback(DetailView):
    template_name = 'feedback/onefeedback.html'
    model = Feedback



class FeedbackDoneView(TemplateView):
    template_name = 'feedback/done.html'