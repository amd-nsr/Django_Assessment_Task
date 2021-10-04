from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Assesment Task Web API')

urlpatterns = [
    path('users/', include('accounts.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('core/', include('core.urls')),
    path('swagger-docs/', schema_view, name='swagger-docs'),
]