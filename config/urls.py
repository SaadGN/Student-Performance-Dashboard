
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('login/',views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('students/',include('students.urls')),
    path('reports/', include('reports.urls')),
    path('dashboard/', include('dashboard.urls')),
    

]
