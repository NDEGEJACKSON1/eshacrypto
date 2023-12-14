from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index' ),
    path('Post/<str:pk>', views.post_details, name='post_details')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)