from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Profile, Link


# Create your views here.
class LinkListView(ListView):
    model = Link
    # default templated called model_list.html -> link_list.html


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")
    # default templated called model_form -> link_form.html
