from django.shortcuts import render


def source_list(request):
    context = {}

    return render(request, "source/list.html", context)
