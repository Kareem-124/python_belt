from django.urls import path     
from . import views

app_name = 'app'
urlpatterns = [
    # Page Section:
    path('', views.index),
    path('success',views.success, name = 'success'),
    path('table',views.table, name = 'table'),
    path('form',views.form, name = 'form'),

    # Process Section
    path('reg_process', views.reg_process, name='reg_process'),   # Registration Process                                    
    path('login_process', views.login_process, name='login_process'),   # Login Process                                    
    path('success_redirect_process', views.success_redirect_process, name='success_redirect_process'),   # Login Process                                    
    path('logout_process', views.logout_process, name='logout_process'),   # Login Process                                    

]