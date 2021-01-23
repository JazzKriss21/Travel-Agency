from django.urls import path, include

from rest_framework.routers import DefaultRouter

from accounts_api import views


router = DefaultRouter()
router.register('profile_api', views.UserProfileViewSet, basename='UserProfile')


urlpatterns = [
path('api/login/', views.UserLoginApiView.as_view()),
path('api/', include(router.urls)),
path('signup/', views.registration_view, name='signup'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
]