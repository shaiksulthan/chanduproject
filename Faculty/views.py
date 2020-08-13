from django.shortcuts import *
from .models import Faculty
from django.shortcuts import HttpResponse
from .forms import *
from django.contrib import messages

# Create your views here.
def index(req):
	return render(req,"Faculty/index.html")
def register(req):
	if req.method=="POST":
		a=req.POST['name']
		b=req.POST['age']
		c=req.POST['branch']
		d=req.POST['phone']
		e=req.POST['email']

		data=Faculty(Name=a,Age=b,Branch=c,Mobile=d,Email=e)
		data.save()
		messages.success(req,"Registration successfully")
		return redirect('show')
		#return render(req,"Faculty/showdata.html",{'a':a,'b':b,'c':c})
	return render(req,"Faculty/register.html")
def about(req):
	return render(req,"Faculty/about.html")
def signup(req):
	form = StudentForm()
	if req.method=='POST':
		form = StudentForm(req.POST)
		form.save()
		return HttpResponse("Record saved Successfull")
	return render(req,'Faculty/signup.html',{'form':form})

def show(req):
	data=Faculty.objects.all()
	return render(req,'Faculty/show.html',{'data':data})
def edit(req,id):
	data = Faculty.objects.get(id=id)
	if req.method=='POST':
		data.Name= req.POST['name']
		data.Age= req.POST['age']
		data.Branch= req.POST['branch']
		data.Mobile= req.POST['phone']
		data.Email= req.POST['email']
		data.save()
		messages.info(req,"Data Updated")
		return redirect('show')
		#return HttpResponse("Updated successfully")
	return render(req,'Faculty/edit.html',{'data':data})

def delete(req,id):
	data= Faculty.objects.get(id=id)
	data.delete()
	messages.warning(req,"Data deleted")
	#return HttpResponse("Record deleted successfully")
	return redirect('show')
