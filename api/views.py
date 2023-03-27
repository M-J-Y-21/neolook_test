# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
import subprocess

class StartRecordingView(APIView):
    def post(self, request):
        # Get recording parameters from the request body
        recording_params = request.data

        # Start recording with ffmpeg
        subprocess.Popen(['ffmpeg', '-f', 'x11grab', '-s', recording_params['resolution'], '-framerate', recording_params['framerate'], '-i', ':0.0', '-c:v', 'libx264', 'output.mp4'])


        return Response({'status': 'Recording started'})

class StopRecordingView(APIView):
    def get(self, request):
        # Stop recording with ffmpeg
        subprocess.Popen(['pkill', '-f', 'ffmpeg'])

        # Save recorded video
        subprocess.Popen(['mv', 'output.mp4', '/path/to/recordings/output.mp4'])

        return Response({'status': 'Recording stopped and saved'})