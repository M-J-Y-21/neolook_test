# urls.py

from django.urls import path
from .views import StartRecordingView, StopRecordingView

urlpatterns = [
    path('start/', StartRecordingView.as_view()),
    path('stop/', StopRecordingView.as_view()),
]
