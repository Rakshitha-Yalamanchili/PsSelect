from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def login(request):
	return render(request,'login.html')
def index(request):
	probs=ProblemStatement.objects.all()
	ps=[]
	for prob in probs:
		n={}
		n['num']=prob.probNo
		n['name']=prob.psname
		n['desc']=prob.description
		ps.append(n)
	print(ps)
	return render(request,'index.html',{'probs':ps})
def default(request):
	return render(request,'default.html')
	
def validate(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		passOrig=Team.objects.get(teamNo=username)
		if passOrig.password == password:
			return redirect('/home')
	return render(request,'login.html')
	