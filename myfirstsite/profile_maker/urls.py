from django.urls import path
from . import views
from myfirstsite import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.create_profile, name = 'create'),
    path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    print('hello Danh')
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)