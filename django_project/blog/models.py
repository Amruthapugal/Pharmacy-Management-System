from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

class Doctor(models.Model) :
	doctor_id = models.CharField(max_length=100, primary_key = True)
	doctor_name = models.TextField()
	speciality = models.TextField(blank = True)
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	
	def __str__(self) :
		return self.doctor_id
 
	def get_absolute_url(self)	:
		return reverse('Doctor-detail', kwargs = {'pk': self.pk})

class Manufacturar(models.Model) :
	company_id = models.CharField(max_length=20, primary_key = True)	
	company_name = models.CharField(max_length=30)
	Address = models.CharField(max_length= 50)
	#state = models.CharField(max_length = 30, default= "")	
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self) :
		return self.company_id

	def get_absolute_url(self) :
		return reverse('company-detail', kwargs= {'pk' : self.pk})

class Manufacturar_detail(models.Model) :
	company_id = models.ForeignKey(Manufacturar, on_delete = models.CASCADE)
	drugs_type = models.CharField(max_length = 30)
	amount_paid = models.CharField(max_length = 15)

	def __str__(self) :
		return self.company_id
	def get_absolute_url(self) :
		return reverse('company')				

class Patient(models.Model) :
	patient_id = models.CharField(max_length=30, primary_key = True)	
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
	blood_group = models.CharField(max_length = 5)
	phone = models.CharField(max_length = 10)
	author = models.ForeignKey(User, on_delete = models.CASCADE)	

	def __str__(self) :
		return self.patient_id

	def get_absolute_url(self) :
		return reverse('patient-detail', kwargs= {'pk' : self.pk})	


class Bill(models.Model) :
	invoice_id = models.CharField(max_length=20, primary_key = True)
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	grand_total = models.CharField(max_length = 15)
	amount_received = models.CharField(max_length = 15)	

	def __str__(self) :
		return self.invoice_id	

	def get_absolute_url(self) :
		return reverse('bill')

class medicines(models.Model) :
	medicine_id = models.CharField(max_length = 20, primary_key= True)
	medicine_name = models.CharField(max_length = 40)
	cost = models.CharField(max_length = 10)
	medicine_type = models.CharField(max_length = 20)	
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self) :
		return self.medicine_id	
	def get_absolute_url(self) :
		return reverse('medicine')		

class employess(models.Model) :
	employee_id = models.CharField(max_length = 10, primary_key = True) 
	employee_name = models.CharField(max_length = 25)
	email = models.CharField(max_length = 20)
	hire_date = models.CharField(max_length = 10)
	salary = models.CharField(max_length = 10)
	phone = models.CharField(max_length = 10)
	

	def __str__(self) :
		return self.employee_id

	def get_absolute_url(self) :
		return reverse('employee')	

