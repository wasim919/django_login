from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HostelAnnouncements

@login_required
def dashboard_index(request):
    announcements = get_list_or_404(HostelAnnouncements, )
    announcements.sort(key = lambda a: a.timestamp, reverse = True)
    # print(announcements)
    return render(request, 'dashboard/index.html', {
    'announcements': announcements
    })

@login_required
def announcement_detail(request, pk):
    announcement = get_object_or_404(HostelAnnouncements, pk = pk)
    return render(request, 'dashboard/announcement.html', {
    'announcement': announcement
    })

@login_required
def profile(request):
    print('hello')
    return render(request, 'dashboard/profile.html')
