from django.shortcuts import render
from django.http import HttpResponse
from .models import temp_Client
# Create your views here.

def home(request):
	client1 = temp_Client()
	client2 = temp_Client()
	client1.First_name = "Faizan"
	client1.Last_name = "Ahmed"
	client2.First_name = "Ahmed"
	client2.Last_name = "Farhan"
	clients = [client1, client2]
	return render(request,'index.html', {'clients':clients})
