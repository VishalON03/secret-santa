import random
import csv
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from .models import Employee, SecretSantaAssignment
from django.views.decorators.csrf import csrf_exempt

def assign_secret_santa(employees, previous_assignments):
    available_recipients = employees[:]
    assignments = {}
    random.shuffle(available_recipients)

    for giver in employees:
        valid_recipients = [
            r for r in available_recipients 
            if r != giver and (giver, r) not in previous_assignments
        ]

        if not valid_recipients:
            return None  # No valid assignments possible

        recipient = random.choice(valid_recipients)
        assignments[giver] = recipient
        available_recipients.remove(recipient)

    return assignments

@csrf_exempt
def upload_employees(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        reader = csv.reader(file.read().decode('utf-8').splitlines())
        next(reader)  # Skip header

        for row in reader:
            Employee.objects.get_or_create(name=row[0], email=row[1])

        return JsonResponse({'message': 'Employees uploaded successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def generate_secret_santa(request):
    if request.method == 'POST':
        employees = list(Employee.objects.all())
        previous_assignments = {(a.employee, a.secret_child) for a in SecretSantaAssignment.objects.all()}

        assignments = assign_secret_santa(employees, previous_assignments)
        if assignments is None:
            return JsonResponse({'error': 'Assignment failed. Try again.'}, status=400)

        with transaction.atomic():
            for giver, recipient in assignments.items():
                SecretSantaAssignment.objects.create(employee=giver, secret_child=recipient, year=2025)

        return JsonResponse({'message': 'Secret Santa assignments completed'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def export_secret_santa(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="secret_santa.csv"'

    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Employee Email', 'Secret Child Name', 'Secret Child Email'])

    for assignment in SecretSantaAssignment.objects.all():
        writer.writerow([assignment.employee.name, assignment.employee.email, assignment.secret_child.name, assignment.secret_child.email])

    return response
