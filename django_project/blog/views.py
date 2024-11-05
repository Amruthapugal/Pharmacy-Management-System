from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.decorators import login_required, permission_required
from .models import Doctor, Manufacturar, Patient, Bill, medicines, Manufacturar_detail, employess
from django.db.models import Q
from django.contrib import messages
import csv, io

# Create your views here.
@login_required
def home(requests) :
	context = {
		'posts' : Doctor.objects.all()
	}
	return render(requests, 'blog/home.html', context)
def homepage(requests) :
	return render(requests,'blog/home.html')

def health(requests) :
	return render(requests, 'blog/healthcare.html')

def Search(requests) :
	if requests.method == 'POST' :
		srch = requests.POST['srh']

		if srch :
			match = Patient.objects.filter(Q(name__icontains = srch) |
										   Q(patient_id__icontains = srch))

			if match :
				return render(requests, 'blog/search.html', {'sr' : match})	
			else :
				messages.error(requests, 'No results found')
		else :
			return HttpResponseRedirect('/search/')

	return render(requests, 'blog/search.html')				

class PostListView(ListView) :
	model = Doctor
	template_name = 'blog/doctor.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5



class PostDetailView(DetailView) :
	model = Doctor



class PostCreateView(LoginRequiredMixin, CreateView) :
	model = Doctor
	fields = ['doctor_id', 'doctor_name', 'speciality']	

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

'''	def test_func(self) :
		Doctor = self.get_object()
		if self.request.user == Doctor.author :
			return True
		return False	'''

class PostUpdateView(LoginRequiredMixin, UpdateView) :
	model = Doctor
	fields = ['doctor_id', 'doctor_name', 'speciality']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin) :
	model = Doctor
	success_url = '/'
	def user_func(self) :
		Doctor = self.get_object()
		if self.request.user == Doctor.author :
			return True
		return False	

################################################  Manufacturar	###############################################

def manufacturar(requests) :
	context1 = {
		'posts_d' : Manufacturar.objects.all()
	}
	return render(requests,'blog/drug_manufacturar.html', context1)
def manufacturar_detail(requests) :
	context_d ={
		'posts_db' : Manufacturar_detail.objects.all()
	}	
	return render(requests,'blog/drug_manufacturar.html', context_d)

class PostListView_d(ListView) :
	model = Manufacturar
	template_name = 'blog/drug_manufacturar.html'
	context_object_name = 'posts_d'
	ordering = ['-date_posted']
	paginate_by = 3	

class PostListView_dm(ListView) :
	model = Manufacturar_detail
	template_name = 'blog/drug_manufacturar.html'	
	context_object_name = 'posts_db'

class PostCreateView_dm(LoginRequiredMixin, CreateView) :
	model = Manufacturar_detail
	fields = ['company_id', 'drugs_type', 'amount_paid']	

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)		



class PostDetailView_d(DetailView) :
	model = Manufacturar



class PostCreateView_d(LoginRequiredMixin, CreateView) :
	model = Manufacturar
	fields = ['company_id', 'company_name', 'Address']	

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)	


class PostUpdateView_d(LoginRequiredMixin, UpdateView)		:
	model = Manufacturar
	fields = ['company_id', 'company_name', 'Address']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView_d(LoginRequiredMixin, UserPassesTestMixin, DeleteView) :
	model = Manufacturar
	success_url = '/drug_manufacturar/'

	def test_func(self) :	
		Manufacturar = self.get_object()
		if self.request.user == Manufacturar.author :
			return True
		return False		
 ############################################################### Patient #################################################

def patient(requests) :
 	context2 = {
 		'posts_p' : Patient.objects.all()
 	}
 	return render(requests,'blog/patient.html', context2)

class PostListView_p(ListView) :
	model = Patient
	template_name = 'blog/patient.html'
	context_object_name = 'posts_p'
	#ordering = ['-date_posted']
	paginate_by = 6
class PostCreateView_p(LoginRequiredMixin, CreateView) :
	model = Patient
	fields = ['patient_id', 'name', 'email', 'doctor', 'blood_group', 'phone']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form) 

class PostDetailView_p(DetailView) :
	model = Patient

class PostUpdateView_p(LoginRequiredMixin, UpdateView) :
	model = Patient
	fields = ['patient_id', 'name', 'email', 'doctor', 'blood_group', 'phone']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView_p(LoginRequiredMixin, DeleteView) :
	model = Patient
	success_url = '/patient/'
	def test_func(self) :
		if self.request.user == Patient.author :
			return True
		return False	


########################################################## Bill ############################################

def bill(requests) :
	context3 = {
		'posts_b' : Bill.objects.all()
	}	
	return render(requests, 'blog/bill.html', context3)			

class PostListView_b(ListView) :
	model = Bill
	template_name = 'blog/bill.html'
	context_object_name = 'posts_b'
	paginate_by = 4

class PostCreateView_b(LoginRequiredMixin,CreateView) :
	model = Bill
	fields = ['invoice_id','patient','date', 'grand_total', 'amount_received']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView_b(LoginRequiredMixin, UpdateView) :
	model = Bill
	fields = ['invoice_id','patient','date', 'grand_total', 'amount_received']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView_b(LoginRequiredMixin, DeleteView) :
	model = Bill
	success_url = '/bill/'
	def test_func(self) :
		if self.request.user == Bill.author :
			return True
		return False

def bill_print(requests) :
	context3 = {
		'posts_b' : Bill.objects.all()
	}	
	return render(requests, 'blog/billprint.html',context3)	

####################################### Medicine ##########################################
def med(requests) :
	context4 = {
		'posts_m' : medicines.objects.all()
	}
	return render(requests, 'blog/medicine.html', context4)

def search_medicines(requests) :
	if requests.method == 'POST' :
		srch = requests.POST['srh']

		if srch :
			match = medicines.objects.filter(Q(medicine_name__icontains = srch) |
										   Q(medicine_id__icontains = srch))

			if match :
				return render(requests, 'blog/search_medicine.html', {'sr' : match})	
			else :
				messages.error(requests, 'No results found')
		else :
			return HttpResponseRedirect('/search_medicine/')

	return render(requests, 'blog/search_medicine.html')				

class PostListView_m(ListView) :
	model = medicines
	template_name = 'blog/medicine.html'
	context_object_name = 'posts_m'
	paginate_by = 6

class PostCreateView_m(LoginRequiredMixin, CreateView) :
	model = medicines
	fields = ['medicine_id','medicine_name','cost', 'medicine_type']
	#form_class = PostForm

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView_m(LoginRequiredMixin, DeleteView) :
	model = medicines
	success_url = '/medicine/'
	def test_func(self) :
		if self.request.user == medicines.author :
			return True
		return False	

def about(requests) :
	return render(requests, 'blog/about.html')	

@permission_required('admin.can_add_log_entry')
def patient_download(requests) :
	items = Patient.objects.all()
	response = HttpResponse(content_type = 'text/csv')
	response['Patient-Disposition'] = 'attachment; filename = patient.csv'
	writer = csv.writer(response, delimiter = ',')		
	writer.writerow(['patient_id', 'name', 'email', 'doctor', 'blood_group', 'phone'])	

	for obj in items :
		writer.writerow([obj.patient_id, obj.name, obj.email, obj. doctor, obj.blood_group, obj.phone])

	return response	

@permission_required('admin.can_add_log_entry')
def bill_download(requests) :
	items = Bill.objects.all()
	response = HttpResponse(content_type = 'text/csv')
	response['Bill-Disposition'] = 'attachment; filename = bill.csv'
	writer = csv.writer(response, delimiter = ',')

	writer.writerow(['invoice_id', 'patient', 'date', 'grand_total', 'amount_received'])

	for obj in items :
		writer.writerow([obj.invoice_id, obj.patient, obj.date, obj.grand_total, obj.amount_received])

	return response	

#@permission_required('admin.can_add_log_entry')
def emp(requests) :
	context5 = {
		'posts_emp' : employee.objects.all()
	}	
	return render(requests, 'blog/employee.html', context5)


class PostListView_e(LoginRequiredMixin, ListView) :
	model = employess
	template_name = 'blog/employee.html'
	context_object_name = 'posts_emp'

class PostCreateView_e(LoginRequiredMixin, CreateView) :
	model = employess
	fields = ['employee_id','employee_name','email', 'hire_date', 'salary', 'phone']
	#form_class = PostForm

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)	

class PostUpdateView_e(LoginRequiredMixin, UpdateView) :
	model = employess
	fields = ['employee_id','employee_name','email', 'hire_date', 'salary', 'phone']

	def form_valid(self, form) :
		form.instance.author = self.request.user
		return super().form_valid(form)		
def upload_bill(requests) :
	template_name = 'blog/bill_upload_csv.html'
	prompt  = {
		'order' : 'order of the csv file should be invoice_id, patient, grand_total, amount_received'
	}

	if requests.method == "GET" :
		return render(requests, template_name, prompt)

	csv_file = requests.FILES['file']
	
	if not csv_file.name.endswith('.csv') :
		messages.error(requests, 'not a csv file')

	data_set = csv_file.read().decode('UTF-8')	

	io_string = io.StringIO(data_set)
	next(io_string)	

	for column in csv.reader(io_string, delimiter = ',', quotechar = '|') :
		__, created = Bill.objects.update_or_create(
			invoice_id = column[0],
			patient = column[1],
			date=  column[2],
			grand_total = column[3],
			amount_received = column[4]
			)
	context5 = {}
	return render(requests, template_name, context)	


def upload_manufacturar(requests) :
	template_name = 'blog/manufacturar_upload_csv.html'
	prompt  = {
		'order' : 'order of the csv file should be medicine_id, medicine_name, cost, medicine_type'
	}

	if requests.method == "GET" :
		return render(requests, template_name, prompt)

	csv_file = requests.FILES['file']
	
	if not csv_file.name.endswith('.csv') :
		messages.error(requests, 'not a csv file')

	data_set = csv_file.read().decode('UTF-8')	

	io_string = io.StringIO(data_set)
	next(io_string)	

	for column in csv.reader(io_string, delimiter = ',', quotechar = '|') :
		__, created = employess.objects.update_or_create(
			employee_id = column[0],
			employee_name = column[1],
			email =  column[2],
			hire_date = column[3],
			salary = column[4],
			phone = column[5]

			)
	context5 = {}
	return render(requests, template_name, context5)	







'''def types(request):
    med_id = request.GET.get('medicine_type')
    med_types = medicines.objects.filter(med_id=med_id).order_by('medicine_type')
    return render(request, 'blog/city_dropdown_list_options.html', {'cities': cities})		'''	








	
'''@property
def foo(self):
	return self.grand_total - self.amount_received '''

			


'''def create(requests) :
	return render(requests, 'blog/cra.html')''' 	
	


		









































	


