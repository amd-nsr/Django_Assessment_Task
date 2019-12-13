from django.urls import path
from core import views
from .views import FileUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload-file/', views.upload_file, name='upload-file'),
    path('dist-calc/', views.dist_calc, name='dist-calc'),
    path('upload-file-api', FileUploadView.as_view()),
    path('browser-server-info/', views.browser_server_info, name='browser-server-info'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)