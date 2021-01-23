from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UploadView as uploader_views

from . import views


urlpatterns = [

    path('api/', include('travelpartner.api.urls')),
    path('',views.travelpartner,name='travel_partner_home'),
    path('details-form/',views.travelpartner_form,name='partner'),
    path('details-view/',views.view_partners,name='partners-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)