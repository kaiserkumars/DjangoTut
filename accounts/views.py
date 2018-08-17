from django.shortcuts import render, HttpResponse

# Create your views here.
# django has two types of views - class based and function based. Class based is complex so we will use function based.
def home(request):
	nums = [1,2,3,4]
	name = "Deepak Kumar"
	args = {"myName":name,"numbers":nums}
	return render(request,'accounts/home.html',args)