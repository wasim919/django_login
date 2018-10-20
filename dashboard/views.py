from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HostelAnnouncements
from accounts.models import Student
from django.contrib.auth.models import User
from .forms import EditProfileForm

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
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data = request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'dashboard/edit_profile.html', {
            'form': form
        })

@login_required
def change_avatar(request, flag):
    if flag == 0:
        pass
    elif flag == 1:
        pass
