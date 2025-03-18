import csv
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa_project.settings")
django.setup()

from secret_santa.models import Employee, SecretSantaAssignment

def load_previous_assignments(csv_path, year=2023):
    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            giver_name, giver_email, child_name, child_email = row

            giver, _ = Employee.objects.get_or_create(name=giver_name.strip(), email=giver_email.strip())
            child, _ = Employee.objects.get_or_create(name=child_name.strip(), email=child_email.strip())

            SecretSantaAssignment.objects.create(employee=giver, secret_child=child, year=year)

        print(f"✅ Previous assignments for {year} loaded successfully!")

if __name__ == "__main__":
    csv_file = "uploads/Secret-Santa-Game-Result-2023.csv"
    if os.path.exists(csv_file):
        load_previous_assignments(csv_file, 2023)
    else:
        print("❌ File not found:", csv_file)
