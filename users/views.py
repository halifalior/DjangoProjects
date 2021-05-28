
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm ,UserProfileForm

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        profile_form = UserProfileForm()
        context = {'form':form , 'profile_form':profile_form}
        return render(
            request, "register.html",
            context
        )
    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():

            user = form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            login(request, user)
            return redirect(reverse("home"))