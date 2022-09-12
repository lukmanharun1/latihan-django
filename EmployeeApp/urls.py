# from django.conf.urls import url
from EmployeeApp import views
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.employeeApi),
    path('employee/<slug:id>',views.employeeApi),

    re_path(r'^employee/savefile',views.saveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)