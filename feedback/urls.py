from django.urls import path
from .views import FeedbackView, FeedbackUpdateView, FeedbackDoneView, ListFeedback, DetailFeedback

urlpatterns = [
    path('feedbacks/', ListFeedback.as_view()),
    path('feedback/<int:pk>/', DetailFeedback.as_view()),
    path('done/', FeedbackDoneView.as_view()),
    path('<int:pk>/', FeedbackUpdateView.as_view()),
    path('', FeedbackView.as_view()),
]