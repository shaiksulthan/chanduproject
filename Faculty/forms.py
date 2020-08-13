from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
	class Meta:
		model=Faculty
		#fields = ['Name','Branch']
		fields = '__all__' #all fields