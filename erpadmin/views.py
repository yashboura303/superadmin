from django.shortcuts import render
from .models import SchoolErp
from django.contrib import messages
# Create your views here.
def add_admin(request):
    if request.method=="POST":
        school_url = request.POST.get("school_url")
        school = request.POST.get("school")
        admin_username = request.POST.get("admin_username")
        admin_password = request.POST.get("admin_password")
        if school and school_url and admin_password and admin_password:
            SchoolErp.objects.create(school=school, school_url=school_url, admin_username=admin_username, admin_password=admin_password)
            messages.success(request, "Record Added")
    return render(request,"erpadmin/add_admin.html")

def view_admins(request):
    erps = SchoolErp.objects.all()
    context = {
        "erps":erps
    }
    return render(request, "erpadmin/view_admins.html", context)