# **Secret Santa Django Project**

## **📌 Overview**

This Django-based project automates the **Secret Santa** gift exchange. It assigns each employee a **Secret Santa recipient** while ensuring that no one is assigned the same recipient as the previous year.

## **📂 Project Structure**

secret\_santa\_project/  
│── secret\_santa\_project/       \# Django project configuration  
│── secret\_santa/               \# Main app (models, views, URLs)  
│── scripts/                    \# Standalone Python scripts  
│── uploads/                    \# CSV file storage  
│── templates/                   \# HTML templates (index.html)  
│── static/                      \# Static files (CSS, JS)  
│── requirements.txt             \# Dependencies list  
│── README.md                    \# Documentation  
│── manage.py                     \# Django management script

---

## **⚡ Setup Instructions**

### **1️⃣ Install Dependencies**

Make sure you have **Python 3.8+** installed. Then, install required packages:

pip install \-r requirements.txt

### **2️⃣ Apply Migrations**

python manage.py makemigrations  
python manage.py migrate

### **3️⃣ Run the Django Server**

python manage.py runserver

Now, open [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/) in your browser.

---

## **📤 Upload CSV Files**

Before generating Secret Santa assignments, you need to upload the **employee list** and **previous year’s assignments**.

### **Upload Employee List (CSV)**

python scripts/load\_employees.py

### **Upload Previous Assignments (CSV)**

python scripts/load\_previous\_assignments.py

### **Generate Secret Santa Assignments**

python scripts/generate\_assignments.py

### **Export Secret Santa Assignments**

python scripts/export\_assignments.py

The results will be saved in **uploads/secret\_santa\_2024.csv**.

---

## **🚀 API Endpoints (Optional)**

| Action | Method | Endpoint |
| ----- | ----- | ----- |
| Upload Employee List | `POST` | `/secret_santa/upload/` |
| Upload Previous Assignments | `POST` | `/secret_santa/upload_previous_assignments/` |
| Generate Assignments | `POST` | `/secret_santa/generate/` |
| Export Assignments | `GET` | `/secret_santa/export/` |

---

## **🎁 Next Steps**

* **Add Email Notifications 📧**  
* **Deploy on a Cloud Platform (AWS, Heroku) 🌍**  
* **Use a Database (PostgreSQL, MySQL) instead of SQLite**

---

### **Need Help?**

If you have any issues, feel free to reach out\!

---

