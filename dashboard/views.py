from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import HostelAnnouncements

@login_required
def dashboard_index(request):
    announcements = get_list_or_404(HostelAnnouncements, )[:5]
    announcements.sort(key = lambda a: a.timestamp, reverse = True)
    return render(request, 'dashboard/index.html', {
    'announcements': announcements
    })
