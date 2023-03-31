from django.urls import path
# from .views import FeedbackView, FeedbackUpdateView, FeedbackDoneView, ListFeedback, DetailFeedback
from . import views

urlpatterns = [
    path('feedbacks/done/', views.done),
    path('feedbacks/<int:id_feedback>/', views.feedback_update),
    path('feedbacks/', views.feedback),
]
