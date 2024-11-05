from django.urls import path
from . import views
from .views import (
 PostListView, 
 PostDetailView, 
 PostCreateView, 
 PostUpdateView, 
 PostDeleteView, 
 PostListView_d,
 PostListView_dm, 
 PostCreateView_d,
 PostDetailView_d,
 PostUpdateView_d,
 PostDeleteView_d,
 PostListView_p,
 PostCreateView_p,
 PostDetailView_p,
 PostUpdateView_p,
 PostDeleteView_p,
 PostListView_b,
 PostCreateView_b,
 PostUpdateView_b,
 PostDeleteView_b,
 PostListView_m,
 PostCreateView_m,
 PostDeleteView_m,
 PostCreateView_dm, 
 patient_download,
 bill_download,
 PostListView_e,
 PostCreateView_e,
 PostUpdateView_e,
 upload_bill,
 upload_manufacturar
 	)

urlpatterns = [

		path('Doctor/', PostListView.as_view(), name = 'blog-home'),
		path('Doctor/new/', PostCreateView.as_view(), name = 'Doctor-view'),
		path('Doctor/<slug:pk>/', PostDetailView.as_view(), name = 'Doctor-detail'),
		path('Doctor/<slug:pk>/update/', PostUpdateView.as_view(), name = 'Doctor-update'),
		path('Doctor/<slug:pk>/delete/', PostDeleteView.as_view(), name = 'Doctor-delete'),
		path('', views.homepage, name ='blog-homepage'),
		path('healthcare/', views.health, name= 'health'),
		path('about/', views.about, name = 'about-us'),
		path('search/', views.Search, name = 'search'),
		path('search_medicine/', views.search_medicines, name = 'search-medicine'),
		path('download-csv', patient_download, name = 'patient-download'),
		path('download-summary', bill_download, name = 'download-summary'),
		path('upload-bill/', upload_bill, name = 'upload-bill'),
		path('upload-manufactuar/', upload_manufacturar, name = 'upload-manufacturar'),

		path('drug_manufacturar/', PostListView_d.as_view(), name = 'company' ),
		path('drug_manufacturar/', PostListView_dm.as_view(), name = 'company' ),
		path('drug_manufacturar/new/', PostCreateView_d.as_view(), name = 'company-view'),
		path('drug_manufacturar/new1/', PostCreateView_dm.as_view(), name = 'manufaturar_detail'),
		path('drug_manufacturar/<slug:pk>/', PostDetailView_d.as_view(), name = 'company-detail'),
		path('drug_manufacturar/<slug:pk>/update/', PostUpdateView_d.as_view(), name = 'company-update'), 
		path('drug_manufacturar/<slug:pk>/delete/', PostDeleteView_d.as_view(), name = 'company-delete'),

		path('patient/', PostListView_p.as_view(), name = 'patient' ),
		path('patient/new/', PostCreateView_p.as_view(), name = 'patient-view'),
		path('patient/<slug:pk>/', PostDetailView_p.as_view(), name = 'patient-detail'),
		path('patient/<slug:pk>/update/', PostUpdateView_p.as_view(), name = 'patient-update'), 
		path('patient/<slug:pk>/delete/', PostDeleteView_p.as_view(), name = 'patient-delete'),

		path('bill/', PostListView_b.as_view(), name = 'bill'),
		path('bill/new/', PostCreateView_b.as_view(), name = 'bill-create'),
		#path('bill/<slug:pk>/', PostDetailView_b.as_view(), name = 'bill-detail'),
		path('bill/<slug:pk>/update/', PostUpdateView_b.as_view(), name = 'bill-update'),
		path('bill/<slug:pk>/delete/', PostDeleteView_b.as_view(), name = 'bill-delete'),
		path('bill/print/', views.bill_print, name = 'bill-print'),

		path('medicine/', PostListView_m.as_view(), name = 'medicine' ),
		path('medicine/new/', PostCreateView_m.as_view(), name = 'medicine-view'),
		path('medicine/<slug:pk>/delete/', PostDeleteView_m.as_view(), name = 'medicine-delete'),

		path('employee/', PostListView_e.as_view(), name = 'employee' ),
		path('employee/new/', PostCreateView_e.as_view(), name = 'employee-view'),
		path('employee/<slug:pk>/update/', PostUpdateView_e.as_view(), name = 'employee-update'),


		
	
]