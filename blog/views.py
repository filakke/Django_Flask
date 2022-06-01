from django.shortcuts import render
from .models import Post

"""posts = [
    {
        'author': 'Diallo',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Juit 28, 2022'
    },
    {
        'author': 'Dicko ',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'Juin 08, 2022'
    }
]"""


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
