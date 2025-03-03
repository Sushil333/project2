import json
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.base import View
import uuid 
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalUpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


from .forms import (
    ChildForm,
    CommonFormForm,
)

from .models import (
    Child,
    CommonForm
)

from schools.models import School

User = get_user_model()


##
## Dashboard
##
@login_required(login_url='login')
def home(request):
    schools_count = School.objects.count()
    context = {
        'dashboard': "active",
        'school_count': schools_count
    }
    return render(request, 'student_parents/index1.html', context=context)


##
## User profile
##
@login_required(login_url='login')
def profile(request):
    try:
        is_update_available = get_object_or_404(Child, user=request.user)
        if is_update_available:
            context = {
                'is_update_available':True,
                'is_student_detail_show':False
            }
    except:
        context = {
            'is_update_available':False,
            'is_student_detail_show':True
        }
    return render(request, 'student_parents/user_profile.html',context=context)


@login_required(login_url='login')
def profile_update(request,pk):
    if request.is_ajax and request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile_no = request.POST['mobileno']

        instance = User.objects.get(pk=pk)
        instance.first_name = firstname
        instance.last_name = lastname
        instance.mobile_no = mobile_no
        instance.save()

        return JsonResponse({
            'first_name': instance.first_name, 
            'last_name': instance.last_name,
            'mobile_no': instance.mobile_no
            }, status=200)
    return JsonResponse({'message': 'Operation failed'}, status=400)


##
# Manage child
##
class ManageChild(LoginRequiredMixin ,View):
    form_class = ChildForm
    template_name = 'student_parents/manage-child.html'

    def get(self, request):
        instance = Child.objects.all()
        context = {'form': ChildForm, 'manage_child': "active", 'data': instance}
        return render(request, self.template_name, context)


class ChildCreateView(BSModalCreateView):
    template_name = 'student_parents/_child-form.html'
    form_class = ChildForm
    success_url = reverse_lazy('manage_child')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChildUpdateView(BSModalUpdateView):
    model = Child
    template_name = 'student_parents/_child-form.html'
    form_class = ChildForm
    success_url = reverse_lazy('manage_child')


class ChildDeleteView(BSModalDeleteView):
    model = Child
    template_name = 'student_parents/_delete-child.html'
    success_url = reverse_lazy('manage_child')


##
## common form
##
class CommonFormView(LoginRequiredMixin, ListView):
    model = Child
    template_name = 'student_parents/common-form-view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['common_form'] = 'active'
        return context


class CommonFormCreateOrUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'student_parents/common-form.html'
    form_class = CommonFormForm
    success_url = reverse_lazy('common_form_view')

    def get_object(self, queryset=None):
        child = get_object_or_404(Child, id=self.kwargs['pk'])
        obj, created = CommonForm.objects.get_or_create(child=child)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['child'] = get_object_or_404(Child, id=self.kwargs['pk'])
        context['common_form'] = 'active'
        return context
    
    def form_valid(self, form):
        form.instance.child = self.get_context_data()['child']
        return super().form_valid(form)