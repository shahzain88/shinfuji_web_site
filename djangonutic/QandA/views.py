from django.shortcuts import render

# Create your views here.


def QandA_list(request):
    return render(request, "QandA/QandA_list.html")
