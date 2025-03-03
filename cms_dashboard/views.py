from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from django.core import serializers
from django.views.generic.list import ListView

from cms_dashboard.forms import ImportFileForm
from cms_dashboard.models import CSVFile
from schools.models import *
from schools.forms import *

## cms view only
class CmsDashboard(View):
    def get(self, request):
        return render(request, 'cms_dashboard/index1.html', {'dashboard': 'active'})


## upload csv
from django.core.paginator import Paginator
def upload_csv(request):
    template_name = 'cms_dashboard/upload-csv.html'

    if request.method == 'POST':
        form = ImportFileForm(request.FILES)

        if form.is_valid():
            form.save()
            return redirect('employee_dashboard')
        else:
            return render(request, template_name, {'form': form})

    form = ImportFileForm()    
    school_list = School.objects.all().order_by('school_name')
    paginator = Paginator(school_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name, {'form':form, 'page_obj': page_obj})


class UploadHistory(ListView):
    template_name = 'cms_dashboard/upload-history.html'
    paginate_by = 10
    model = CSVFile
    ordering = ['-upload_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['csv_upload'] = 'active'
        return context


    
## employee school info
def employee_school_info(request, school_id):
    if request.method == 'POST':
        instance = School.objects.get(id=school_id)
        form = school_addForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            instance = School.objects.get(id=school_id)
            form = school_addForm(instance=instance)
            fee_data = SchoolFee.objects.filter(school=instance)
            return render(request, 'employee/school_form.html', {'school_form': form, 'instance': instance, 'fee_data': fee_data, 'School_Information' : 'active'})
    else:
        instance = School.objects.get(id=school_id)
        fee_data = SchoolFee.objects.filter(school=instance)
        form = school_addForm(instance=instance)
        return render(request, 'employee/school_form.html', {'school_form': form, 'instance': instance, 'fee_data': fee_data})
    

## school facilities
def school_facilities(request, school_id):
    if request.method == 'POST':
        instance = School.objects.get(id=school_id)
        form = school_fc_Form(request.POST)
        if form.is_valid():
            return redirect('employee_school_facilities')
    else:
        instance = School.objects.get(id=school_id)
        school_facilities = SchoolFacilities.objects.get(school=instance)
        form = school_fc_Form(instance=school_facilities)
        return render(request, 'employee/school_facilities.html', {'school_fc_form': form, 'instance':instance, 'employee_school_facilities': 'active'})
    

## school fees
class SchoolFeesView(View):
    def get(self, request, *args, **kwargs ):
        school_id = self.kwargs['school_id']
        school_instance = School.objects.get(id=school_id)
        school_fee_instance = SchoolFee.objects.filter(school=school_instance)
        serialized_data = serializers.serialize('json', school_fee_instance)
        return JsonResponse({'data': serialized_data}, status=200)
        
    def post(self, request, *args, **kwargs):
        print('in post')
        standard = request.POST.get('standard')
        fee_name = request.POST.get('fee-name')
        fee_amount = request.POST.get('fee-amount')
        school_id = request.POST.get('school_id')
        fee_id = request.POST.get('fee-id')
        try:
            school_instance = School.objects.get(id=school_id)
            if not fee_id or fee_id == '':
                school_fee_instance = SchoolFee.objects.create(
                    school=school_instance, 
                    standard=standard,
                    fee_name=fee_name, 
                    fee_amount=fee_amount
                )
                d = serializers.serialize('json', [school_fee_instance])
                return JsonResponse({'message': 'Added successfully', 'data': d}, status=201)
            else:
                instance = SchoolFee.objects.get(pk=fee_id)
                instance.fee_name = fee_name
                instance.fee_amount = fee_amount
                instance.save()
                d = serializers.serialize('json', [instance])
                return JsonResponse({'message': 'Updated successfully', 'data': d}, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Server error'}, status=400)


## school fees delete
class SchoolFeeDelete(View):
    def post(self, request):
        _id = request.POST.get('id')
        SchoolFee.objects.get(pk=_id).delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=201)
    

## Hall of fame
class SchoolFameView(View ):
    def get(self, request, school_id):
        instance = School.objects.get(id=school_id)
        return render(request, "employee/hall_of_fame.html", {'instance':instance, 'employee_school_fame': 'active'})


## hall of fame add
class HallofFameAdd(View):
    def get(self, request, school_id):
        school_instance = School.objects.get(id=school_id)
        instance = HallofFame.objects.filter(school=school_instance)
        sr_data = serializers.serialize('json', instance)
        return JsonResponse({'data': sr_data}, status=200)
    
    def post(self, request, school_id):
        fame_title = request.POST.get('fame-title')
        fame_id = request.POST.get('fame-id')
        try:
            school_instance = School.objects.get(id=school_id)
            if not fame_id or fame_id == '':
                school_fame_instance = HallofFame.objects.create(
                    school=school_instance, 
                    title=fame_title, 
                )
                d = serializers.serialize('json', [school_fame_instance])
                return JsonResponse({'message': 'Added successfully', 'data': d}, status=201)
            else:
                instance = HallofFame.objects.get(pk=fame_id)
                instance.title = fame_title
                instance.save()
                d = serializers.serialize('json', [instance])
                return JsonResponse({'message': 'Updated successfully', 'data': d}, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Server error'}, status=400)


## hall of fame delete
class HallofFameDelete(View):
    def post(self, request):
        _id = request.POST.get('id')
        HallofFame.objects.get(pk=_id).delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=201)
    

## school gallery view only
class SchoolGalleryView(View):
    def get(self, request):
        school_gallery = SchoolGallery.objects.all()
        return render(request, 'school_dashboard/school_gallery.html', {'school_gallery': school_gallery})

    def post(self, request):
        try:
            school_instance = School.objects.get(owner=request.user)
            img = request.FILES['school-img']
            if not img:
                return HttpResponse('img not provied')
            instance = SchoolGallery(school=school_instance, school_img=img)
            instance.save()
            return redirect('school_gallery')
        except Exception as e:
            print(e)
            return HttpResponse('You are not authorized!')