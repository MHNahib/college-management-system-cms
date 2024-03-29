"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

handler404 = 'accounts.views.handler404'

urlpatterns = [
    
    # path('test/', views.test, name='test'),
    # API
    path('user/list/', views.user_list, name='user-list'),

    # LOGIN AND LOGOUT
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ADMISSION
    path('admission/hsc/', views.signup_hsc, name='signup'),
    path('admission/honours/', views.signup_honours, name='signup-h'),   
    path('admission/ibm/', views.signup_ibm, name='signup-ibm'),   
    path('admission/degree/', views.signup_degree, name='signup-degree'),   

    # ADMIN DASHBOARD and student dashboard
    path('dashboard/', views.admin_dashboard, name='admin'),
    path('student/', views.student_dashboard, name='dashboard'),

    # ADD TEACHER PRINCIPAL AND STAFFS
    path('add/principal/', views.add_principal, name='add-principal'),
    path('add/teacher/', views.add_teacher, name='add-teacher'),
    path('add/staff/', views.add_staff, name='add-staff'),

    # EDIT TEACHER AND STAFF
    path('edit/staff/<str:id>/', views.edit_staff, name='edit-staff'),
    path('edit/teacher/<str:id>/', views.edit_teacher, name='edit-teacher'),

    # STUDENTS PROFILE AND EDIT
    path('profile/<str:id>/', views.profile, name='show-profile'),
    path('profile/edit/<str:id>/', views.profile_edit, name='edit-profile'),

    # DOWNLOAD FORM
    path('download/<str:username>/', views.download_form, name='download'),
    # path('dashboard/teacher/appoint/<str:id>/', views.wil_take, name='will-take'),

    # STAFF AND TEACHER LIST
    path('list/teachers/', views.teachersList, name='show-teachers-list'),
    path('list/staffs/', views.staffsList, name='show-staffs-list'),

    # ADD NOTICE PHOTO DEPERTMENT SUBJECT SESSION 
    path('add/notice/', views.notice, name='add-notice'),
    path('add/photo/', views.photo, name='add-photo'),
    path('add/books/', views.books, name='add-books'),
    # path('add/depertment/', views.depertment, name='add-depertment'),
    # path('add/subject/', views.subject, name='add-subject'),
    path('add/session/', views.session, name='session'),

    # ADD ROLL 
    path('add/roll/hsc/science/', views.roll_hsc_science, name='roll-hsc-science'),
    path('add/roll/hsc/business-studies/', views.roll_hsc_commarts, name='roll-hsc-commarts'),
    path('add/roll/hsc/humanities/a/', views.roll_hsc_arts_a, name='roll-hsc-Humanities(A)'),
    path('add/roll/hsc/humanities/b/', views.roll_hsc_arts_b, name='roll-hsc-Humanities(B)'),
    path('add/roll/honours/bangla/', views.roll_honours_bangla, name='roll-honours-bangla'),
    path('add/roll/honours/accounting/', views.roll_honours_accounting, name='roll-honours-accounting'),
    path('add/roll/honours/geography/', views.roll_honours_geography, name='roll-honours-geography'),
    path('add/roll/honours/management/', views.roll_honours_management, name='roll-honours-management'),
    path('add/roll/degree/bba/', views.roll_degree_bba, name='roll-degree-bba'),
    path('add/roll/degree/ba/', views.roll_degree_ba, name='roll-degree-ba'),
    path('add/roll/degree/bss/', views.roll_degree_bss, name='roll-degree-bss'),
    path('add/roll/ibm/', views.roll_ibm, name='roll-ibm'),

    # API 
    path('add/roll/', views.add_roll, name='add-roll'),

    # ADD AND SHOW SESSION 
    path('add/session/save/', views.session_save, name='save_session'),
    path('add/session/show/', views.session_show, name='show_session'),

    # ADD YEAR 
    path('add/year/', views.year, name='year'),

    # PAYMENT 
    path('payment/', views.monthly_payment, name='monthly-payment'),

    # SEARCH 
    path('payment/search/', views.payment_search, name='search-payment'),
    path('edit/search/', views.edit_search, name='edit-payment'),
    path('update-year-search/', views.update_year_search, name='update-student-search'),
    path('update/year/', views.update_year, name='update-student'),


    path('payment/donation/', views.get_donation, name='donation'),
    path('payment/<str:id>/', views.payment, name='payment'),
    path('pardon/<str:id>/', views.pardon , name='pardon'),
    path('expense/', views.expense , name='expense'),
    path('ladger/search/', views.ladger_search , name='ladger-search'),

    path('display/income/', views.display_income , name='income-expences'),

    # path('list/students/', views.list_students , name='list-students'),
    
    # path('add/notice/', views.notice, name='add-staff'),

    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    
]


