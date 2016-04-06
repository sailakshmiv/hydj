from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from .models import Contents

def index(request):
    page_list = Contents.objects.all()
    context = {
        'page_list': page_list
    }
    if request.GET.__contains__("ids"):
        context["detail_item"] = Contents.objects.get(pk=request.GET["ids"])
    
    return render(request, "hydj/index.html", context)
    
def detail(request, ids):
    page_detail = Contents.objects.get(pk=ids)
    context = {
        'page_detail': page_detail
    }
    return render(request, "hydj/detail.html", context)