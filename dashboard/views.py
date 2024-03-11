from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import time
import os

from django.http import JsonResponse

from django.db import connections

from django.http import HttpResponse

# import pyarrow
# import fastparquet

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')