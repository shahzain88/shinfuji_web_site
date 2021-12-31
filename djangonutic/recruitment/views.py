from django.shortcuts import render

# Create your views here.


def recruitment_list(request):
    return render(request, "recruitment/recruitment_list.html")
