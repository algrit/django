from .forms import FeedbackForm
from .models import Feedback
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DetailView, ListView
from django.db.models import Q, F


# class FeedbackView(FormView):
#     """Comment form with usage FormView class"""
#     form_class = FeedbackForm
#     template_name = 'feedback/index.html'
#     success_url = 'done'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    success_url = 'done'


class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    success_url = '/feedbacks/done'


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback/detail.html'


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback/list.html'

    def get_queryset(self):
        """Changing default queryset with filters and/or order if needed"""
        queryset = super().get_queryset().filter(Q(rating__gte=5)).order_by(F('name').asc(nulls_last=True))
        return queryset


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        """Sending additional information if needed"""
        context = super().get_context_data(**kwargs)
        context['new_data'] = 'test'
        return context
