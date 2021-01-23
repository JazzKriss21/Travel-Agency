from django.urls import path, include
from . import views
urlpatterns = [
    path('api/', include('crowdfund.api.urls')),
    path('fund/',views.crowdfund),
    path('campaign',views.campaign,name="campaign"),
]