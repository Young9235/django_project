from django.shortcuts import render

# Create your views here.
from .models import Video
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import VideoForm


class VideoListView(ListView):
    queryset = Video.objects.all()
    # all_count = Video.objects.all().count()
    #print(queryset)
    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)   #super:부모?
        # context['count'] = 4
        context['all_count'] = Video.objects.all().count()
        return context

class VideoDetailView(DetailView):
    queryset = Video.objects.all()          #video의 모든 걸 가져온다는 의미

    def get_context_data(self, *arg, **kwargs):
        context = super(VideoDetailView, self).get_context_data(*arg, **kwargs)
        return context

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    success_url = '/video/'

    def form_valid(self, form):
        # print('form_valid')
        # print(self.request.POST.get('title'))
        # print(self.request.POST.get('embed_code'))
        return super(VideoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # print('form_in_valid')
        # print(self.request.POST.get('title'))
        # print(self.request.POST.get('embed_code'))
        return super(VideoCreateView, self).form_invalid(form)

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm

class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = '/video/'
