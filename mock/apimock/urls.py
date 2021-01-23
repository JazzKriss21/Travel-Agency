from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.homepage_view, name="homepage_view"),
    path('shop',views.shop_view, name="shop_view"),
    path('travelpartner',views.travelpartner_view, name="travelpartner_view"),
    path('crowdfund',views.crowdfund_view, name="crowdfund_view")
]