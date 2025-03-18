import random
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa_project.settings")
django.setup()

from secret_santa.models import Employee, SecretSantaAssignment

def assign_secret_santa(year=2024):
    employees = list(Employee.objects.all())
    previous_assignments = {(a.employee, a.secret_child) for a in SecretSantaAssignment.objects.filter(year=year-1)}

    available_recipients = employees[:]
    assignments = {}

    random.shuffle(available_recipients)

    for giver in employees:
        valid_recipients = [
            r for r in available_recipients 
            if r != giver and (giver, r) not in previous_assignments
        ]

        if not valid_recipients:
            print("❌ No valid assignments possible. Try again.")
            return

        recipient = random.choice(valid_recipients)
        assignments[giver] = recipient
        available_recipients.remove(recipient)

    for giver, recipient in assignments.items():
        SecretSantaAssignment.objects.create(employee=giver, secret_child=recipient, year=year)

    print(f"✅ Secret Santa assignments for {year} completed!")

if __name__ == "__main__":
    assign_secret_santa(2024)
