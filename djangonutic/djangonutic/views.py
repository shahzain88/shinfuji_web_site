from django.http import HttpResponse
from django.shortcuts import render

def view_robot_txt(request):
    return render(request, "robots.txt")
def view_404(request):
    return render(request, "404.html")

def homepage(request):
    # return HttpResponse("Home or / ")
    return render(request, "homepage.html")


def about(request):
    # return HttpResponse('About')
    return render(request, "about.html")
