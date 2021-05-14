from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = post 

class PostDatailView(DetailView):
    model = Post

# Create your views here.
