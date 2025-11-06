from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from gym.views import register_view, forgot_password
from gym.views import (
     admin_login_view, Home, About, Contact,
    Add_Enquiry, View_Enquiry, Delete_Enquiry, Edit_Enquiry,
    Add_Equipment, View_Equipment, Delete_Equipment, Edit_Equipment,
    Add_Plan, View_Plan, Delete_Plan, Edit_Plan,
    Add_Member, View_Member, Delete_Member, Edit_Member,
)
from django.contrib.auth import views as auth_views # pyright: ignore[reportMissingModuleSource]
# In GMS/GMS/urls.py
from gym.views import forgot_password

urlpatterns = [
    # ... other urls


    path('admin-login', admin_login_view, name='admin_login'),
    path('admin/', admin.site.urls),
       path('forgot_password/', forgot_password, name='forgot_password'),
    # ... other urls

    path('register/', register_view, name='register'),
    # Use built-in auth views: login at root, redirect to /home/ on success (LOGIN_REDIRECT_URL)
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),

    # Keep an admin-login alias if needed
    path('admin_login/', admin_login_view, name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('add_enquiry/', Add_Enquiry, name='add_enquiry'),
    path('view_enquiry/', View_Enquiry, name='view_enquiry'),
    path('delete_enquiry/<int:pid>/', Delete_Enquiry, name='delete_enquiry'),
    path('edit_enquiry/<int:pid>/', Edit_Enquiry, name='edit_enquiry'),

    path('add_equipment/', Add_Equipment, name='add_equipment'),
    path('view_equipment/', View_Equipment, name='view_equipment'),
    path('delete_equipment/<int:pid>/', Delete_Equipment, name='delete_equipment'),
    path('edit_equipment/<int:pid>/', Edit_Equipment, name='edit_equipment'),

    path('add_plan/', Add_Plan, name='add_plan'),
    path('view_plan/', View_Plan, name='view_plan'),
    path('delete_plan/<int:pid>/', Delete_Plan, name='delete_plan'),
    path('edit_plan/<int:pid>/', Edit_Plan, name='edit_plan'),

    path('add_member/', Add_Member, name='add_member'),
    path('view_member/', View_Member, name='view_member'),
    path('delete_member/<int:pid>/', Delete_Member, name='delete_member'),
    path('edit_member/<int:pid>/', Edit_Member, name='edit_member'),
]
