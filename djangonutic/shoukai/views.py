from django.shortcuts import render

# Create your views here.


def shoukai_list(request):
    return render(request, "shoukai/shoukai_list.html")
