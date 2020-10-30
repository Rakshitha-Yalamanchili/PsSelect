from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *

# Create your views here.
def login(request):
	if 'user' in request.session:
		return redirect('/home')
	return render(request,'login.html')
	
def data(request):
	probs=ProblemStatement.objects.all()
	ps=[]
	for prob in probs:
		n={}
		n['num']=prob.probNo
		n['name']=prob.psname
		n['desc']=prob.description
		n['count']=prob.count 
		ps.append(n)
	if request.method=="POST":
		return redirect('/')
	return JsonResponse(ps,safe=False)
		
def index(request):
	if 'user' not in request.session:
		return redirect('/')
	probs=ProblemStatement.objects.all()
	ps=[]
	for prob in probs:
		n={}
		n['num']=prob.probNo
		n['name']=prob.psname
		n['desc']=prob.description
		n['count']=prob.count 
		ps.append(n)
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
	
	return render(request,'index.html',{'probs':ps})
	
	
def validate(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		try:
			passOrig=Team.objects.get(teamNo=username)
			if passOrig.password == password:
				request.session['user']=username
				return redirect('/home')
		except Exception:
			return redirect('/')
	return redirect('/')
	
	
def save(request,pid):
	if 'user' not in request.session:
		return redirect('/')
	ps=ProblemStatement.objects.get(probNo=int(pid))
	if ps.count == 2:
		return redirect('/home')
	team=Team.objects.get(teamNo=int(request.session['user']))
	check=Taken.objects.filter(tNo=team)
	if len(check)>0:
		return redirect('/home')
	a=Taken(tNo=team,psNo=ps)
	a.save()
	p=ProblemStatement.objects.get(probNo=int(pid))
	p.count=p.count+1
	p.save()
	return redirect('/home')