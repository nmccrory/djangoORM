from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.interests.models import Interest, User
# Create your views here.
def index(request):
	users = User.objects.all()

	content = {'users': users}
	return render(request, 'interests/index.html', content)

def show(request, id):
	user = User.objects.get(id=id)

	content = {'user': user}
	return render(request, 'interests/user.html', content)