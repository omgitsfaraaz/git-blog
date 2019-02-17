from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.
def home(request):
	all_posts = Post.objects.all()
	return render(request, "home.html", {'all_posts' : all_posts})

def create_post(request):
	if request.method == "POST":
		title = request.POST['title']
		return HttpResponse(title)

	return render(request, "create.html")
