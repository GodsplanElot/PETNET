from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')
def about(request):
    return render(request, 'core/about.html')