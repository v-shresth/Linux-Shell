from django.shortcuts import render
import subprocess
import cgi

def index(request):
	params = {'command':None}
	if request.POST.get('text'):
		cmd = request.POST.get('text','default')
		command = subprocess.getoutput(cmd)
		params = {'command':command}	
	return render(request, 'index.html', params)


