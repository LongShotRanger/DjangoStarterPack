from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.http import JsonResponse

def index(request):
    return render(request, 'main/homepage.html', {})