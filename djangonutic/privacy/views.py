from django.shortcuts import render

# Create your views here.


def privacy_list(request):
    return render(request, "privacy/privacy_list.html")
