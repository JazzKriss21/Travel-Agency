from django.shortcuts import render,redirect,reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from accounts_api import permissions, serializers, models
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backend = (filters.SearchFilter,)
    search_Fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("/home")
        else:
            print("form is invalid")
            print(form.errors)
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)

def logout_view(request):
    user = request.user
    logout(request)
    return redirect('/home')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        pass
        # return redirect("home")


    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
             email = request.POST['email']
             password = request.POST['password']
             user = authenticate(email=email, password=password)


             if user:
                 login(request, user)
                 # return render(request, 'homepage.html', {
                 #     "email":user.email,
                 # })
                 # return  redirect("/home",{
                 #     "email":user.email,
                 # })

                 return  redirect("/home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "login.html", context)