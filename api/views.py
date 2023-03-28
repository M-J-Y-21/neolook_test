# views.py
import pyautogui
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Recording
from .serializers import RecordingSerializer

class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

    def create(self, request):
        # Start screen recording process
        video_file = 'recordings/{}.mp4'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        pyautogui.screenshot(video_file, fps=30)

        # Save recording details to database
        recording = Recording.objects.create(video_file=video_file)
        serializer = RecordingSerializer(recording)
        return Response(serializer.data)

    def update(self, request, pk=None):
        recording = self.get_object()

        # Stop screen recording process
        # ...

        recording.end_time = datetime.datetime.now()
        recording.save()

        serializer = RecordingSerializer(recording)
        return Response(serializer.data)
