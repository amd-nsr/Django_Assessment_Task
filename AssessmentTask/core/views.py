from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse, HttpResponseRedirect
import googlemaps 
from django.conf import settings
from .forms import UploadFileForm
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .api_keys import GOOGLE_MAPS_API_KEY

def dist_calc(request):
    
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY) 
    dist = gmaps.distance_matrix('Alexandria','Cairo')['rows'][0]['elements'][0] 
    key = GOOGLE_MAPS_API_KEY
    context={
        'dist':dist,
    }
    return render(request, 'dist_calc.html', context)

def browser_server_info(request):
    USER_AGENT = request.META['HTTP_USER_AGENT']
    HTTP_HOST_HEADER = request.META['HTTP_HOST']
    REMOTE_ADDR  = request.META['REMOTE_ADDR']
    REMOTE_HOST = request.META['REMOTE_HOST']
    SERVER_NAME = request.META['SERVER_NAME']
    SERVER_PORT = request.META['SERVER_PORT']

    context={
        'USER_AGENT':USER_AGENT,
        'HTTP_HOST_HEADER':HTTP_HOST_HEADER,
        'REMOTE_ADDR':REMOTE_ADDR,
        'REMOTE_HOST':REMOTE_HOST,
        'SERVER_NAME':SERVER_NAME,
        'SERVER_PORT':SERVER_PORT,
    }
    return render(request, 'browser_server_info.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form })

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
      file_serializer = FileSerializer(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
