from django.shortcuts import render

def index(request):
    return render(request, 'hub/index.html')

def post_detail(request, pk):
    return render(request, 'hub/post_detail.html')

