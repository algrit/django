from django.urls import path
# from .views import FeedbackView, FeedbackUpdateView, FeedbackDoneView, ListFeedback, DetailFeedback
from . import views

urlpatterns = [
    path('feedbacks/done/', views.done),
    path('feedbacks/', views.feedback),
]
