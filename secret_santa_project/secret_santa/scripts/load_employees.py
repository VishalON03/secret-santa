import csv
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa_project.settings")
django.setup()

from secret_santa.models import Employee

def load_employees(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            name, email = row
            Employee.objects.get_or_create(name=name.strip(), email=email.strip())

        print("✅ Employees loaded successfully!")

if __name__ == "__main__":
    csv_file = "uploads/employer-list.csv"
    if os.path.exists(csv_file):
        load_employees(csv_file)
    else:
        print("❌ File not found:", csv_file)
