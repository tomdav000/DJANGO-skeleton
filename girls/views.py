from django.shortcuts import redirect, render
from .models import Girl
from .forms import GirlForm
# Create your views here.
def index(request):
	girls = Girl.objects.all()
	return render(request,'girls/index.html',{'girls': girls})

def new(request):
	form = GirlForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('index');
	return render(request,'girls/new.html',{'form': form})

def girl(request, girl_id):
	girl = Girl.objects.get(id=girl_id)
	return render(request,'girls/girl.html',{'girl': girl})

def edit(request, girl_id):
	girl = Girl.objects.get(id=girl_id)
	form = GirlForm(request.POST or None, instance=girl)
	if form.is_valid():
		form.save()
		return redirect('index');
	return render(request,'girls/edit.html',{'girl': girl, 'form': form})

def delete(request, girl_id):
	girl = Girl.objects.get(id=girl_id)
	if request.method == 'POST':
		girl.delete()
		return redirect('index');
	return render(request,'girls/delete.html',{'girl': girl})
