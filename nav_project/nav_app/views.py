from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'nav/profile.html')

def about(res):
    return render(res, 'nav/about.html')