from django.shortcuts import render
from .models import Friend
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FriendForm

def friend_list(request):
    friends = Friend.objects.all()  
    return render(request, 'my_test/home.html', {'friends': friends})



def add_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('friend_list')
    else:
        form = FriendForm()

    return render(request, 'my_test/add_friend.html', {'form': form})

def delete_friend_page(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    return render(request, 'my_test/delete.html', {'friend': friend})


def delete_friend(request, friend_id):
    if request.method == 'POST':
        friend = Friend.objects.get(id=friend_id)
        friend.delete()
    return redirect('friend_list')

def add_profile(request, friend_id):
    friend = get_object_or_404(Friend, id=friend_id)
    if request.method == 'POST':
        profile_url = request.POST.get('profile')
        friend.profile = profile_url
        friend.save()
        return redirect('friend_list')
    return render(request, 'my_test/Add_profile.html', {'friend': friend})


def delete_profile(request, friend_id):
    if request.method == 'POST':
        friend = get_object_or_404(Friend, id=friend_id)
        friend.profile = None
        friend.save()
    return redirect('friend_list')