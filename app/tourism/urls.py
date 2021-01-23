"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from tourism import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from uploader import views as uploader_views

schema_view = get_schema_view(
   openapi.Info(
      title="Group 22",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts_api.urls')),
    path('shop/', include('shop.urls')),
    path('crowdfund/', include('crowdfund.urls')),
    path('travelpartner/', include('travelpartner.urls')),
    path('home/',views.home_view,name='home'),

    path('home/form/',views.form,name='form_v'),
    path('flight-details/',views.flightdetails_listOfPlaces,name='flight'),
    path('flight-details-routes/',views.flightdetails_place_to_place,name='flight-routes'),
    path('hotel-details/',views.hoteldetails,name='hotels'),
    path('hotel_list/',views.hotel_list,name='list'),
    path('hotel_form/',views.hotel_search),
    path('hotel_details/',views.hotel_detail,name='hotel_d'),
]
