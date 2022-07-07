from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from ssm_app.forms import SignUpForm, PlaylistForm
from ssm_app.models import Song, Playlist


def homepage(request):
    return render(
        request,
        template_name='homepage.html')


def show_music_view(request):
    songs = Song.objects.all()

    return render(
        request,
        template_name='music.html',
        context={'songs': songs})


def show_blog_view(request):
    return render(
        request,
        template_name='blog.html')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('/')


class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('/')


def show_subscription_view(request):
    return render(
        request,
        template_name='subscription.html')


class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist_create.html'
    success_url = reverse_lazy('playlist')

    def form_valid(self, form):
        valid = super().form_valid(form)
        if valid:
            playlist = form.save()
            playlist.user = self.request.user
            playlist.save()
        return valid


class PlaylistListView(ListView):
    model = Playlist
    context_object_name = 'all_playlists'
    template_name = 'playlist_list.html'
