from django.shortcuts import render


def class_info(request):
    context = {}

    return render(request, "class/class.html", context)
