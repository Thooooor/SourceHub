from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user.models import Profile, Student, Teacher


@login_required(login_url="/user/sign-in/")
def index(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.user_type == "student":
        student = Student.objects.get(user=user)

    context = {
        "profile": profile,
        "page": "home",
    }

    return render(request, "home/index.html", context)
