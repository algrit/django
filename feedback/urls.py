from django.urls import path
# from .views import FeedbackView, FeedbackUpdateView, FeedbackDoneView, ListFeedback, DetailFeedback
from . import views

urlpatterns = [
    path('feedbacks/', views.feedback),
]
