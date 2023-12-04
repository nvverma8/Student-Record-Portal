from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Student
from .forms import SATResultForm


# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = SATResultForm(request.POST)
    if form.is_valid():
      # new_student_number = form.cleaned_data['student_number']
      # new_first_name = form.cleaned_data['first_name']
      # new_last_name = form.cleaned_data['last_name']
      # new_email = form.cleaned_data['email']
      # new_field_of_study = form.cleaned_data['field_of_study']
      # new_gpa = form.cleaned_data['gpa']

      # new_student = Student(
        
      #   name=new_first_name,
      #   address=new_last_name,
      #   email=new_email,
      #   field_of_study=new_field_of_study,
      #   gpa=new_gpa
      # )
      form.save()
      return render(request, 'students/add.html', {
        'form': SATResultForm(),
        'success': True
      })
  else:
    form = SATResultForm()
  return render(request, 'students/add.html', {
    'form': SATResultForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = SATResultForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = SATResultForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

def get_rank_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            student = Student.objects.get(name=name)
            student_score = student.sat_score
            rank = Student.objects.filter(sat_score__gt=student_score).count() + 1
            return JsonResponse({'rank': rank})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)