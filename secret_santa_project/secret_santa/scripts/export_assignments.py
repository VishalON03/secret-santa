import csv
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa_project.settings")
django.setup()

from secret_santa.models import SecretSantaAssignment

def export_secret_santa(csv_path, year=2024):
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Employee Name', 'Employee Email', 'Secret Child Name', 'Secret Child Email'])

        for assignment in SecretSantaAssignment.objects.filter(year=year):
            writer.writerow([assignment.employee.name, assignment.employee.email, assignment.secret_child.name, assignment.secret_child.email])

    print(f"✅ Secret Santa assignments for {year} exported to {csv_path}")

if __name__ == "__main__":
    csv_file = "uploads/secret_santa_2024.csv"
    export_secret_santa(csv_file, 2024)
