from django.shortcuts import render

# Create your views here.


def gaiyou_list(request):

    return render(request, "gaiyou/gaiyou_list.html")


def gaiyou_map(request):
    return render(request, "gaiyou/gaiyou_map.html")
