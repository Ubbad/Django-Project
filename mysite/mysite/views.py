#i have created this file
from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1>hello krutik</h1><a href=https://youtube.com/watch?v=PUPok5AZ0ek>Keyboard</a>")

def about(request):
	return HttpResponse("hello krutik solanki")