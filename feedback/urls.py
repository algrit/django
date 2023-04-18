from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import FeedbackView, FeedbackUpdateView, FeedbackDoneView, ListFeedback, DetailFeedback
from . import views

router = SimpleRouter()
router.register('api/feedbacks', views.FeedbackDetailView)


urlpatterns = [
    path('feedbacks/done/', views.DoneView.as_view()),
    path('feedbacks/all/', views.FeedbackListView.as_view()),
    path('feedbacks/change/<int:pk>/', views.FeedbackUpdateView.as_view()),
    # path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view()),
    path('feedbacks/', views.FeedbackCreateView.as_view()),
]

urlpatterns += router.urls
