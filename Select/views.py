from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def login(request):
	return render(request,'login.html')
def index(request):
	tno=Team.objects.get(teamNo=int(request.session['user']))
	taks=Taken.objects.filter(tNo=tno)
	if len(taks)>0:
		psnum=taks[0].psNo.probNo
		ownps=ProblemStatement.objects.get(probNo=psnum)
		own={}
		own['tno']=tno.teamNo
		own['num']=ownps.probNo
		own['name']=ownps.psname
		own['desc']=ownps.description
		return render(request,'default.html',{'own':own})
	probs=ProblemStatement.objects.all()
	ps=[]
	for prob in probs:
		n={}
		n['num']=prob.probNo
		n['name']=prob.psname
		n['desc']=prob.description
		n['count']=prob.count 
		ps.append(n)
	print(ps)
	return render(request,'index.html',{'probs':ps})
	
def validate(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		passOrig=Team.objects.get(teamNo=username)
		if passOrig.password == password:
			request.session['user']=username
			return redirect('/home')
	return redirect('/')
	
	
def save(request,pid):
	ps=ProblemStatement.objects.get(probNo=int(pid))
	team=Team.objects.get(teamNo=int(request.session['user']))
	a=Taken(tNo=team,psNo=ps)
	a.save()
	return redirect('/home')