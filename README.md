# 🎓 Student Internship Management Portal

A full-stack Django web application that allows students to explore and apply for internships, and enables admins to manage internships and applications through a secure admin panel.

---

## 🚀 Features

### 👨‍🎓 Student Side

- View available internships
- Apply for internships with:
  - Name
  - Email
  - Address
  - Resume upload (PDF)
- Clean and responsive UI
- Displays applied internship name on success page
- Auto-redirect after successful application

### 🧑‍💼 Admin Side

- Add, update, delete internships
- View student applications
- Download resumes
- Manage data using Django Admin

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **ORM:** Django ORM
- **File Uploads:** Django Media Handling
- **Version Control:** Git & GitHub

---

## 📸 Screenshots

### 🏠 Internship Listings Page
![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS1.jpg)

![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS2.jpg)

![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS3.jpg)

![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/Screenshot%202025-12-18%20202916.jpg)






---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Prince1587/-Student-Internship-Management-Portal.git
cd Student_internship_portal
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
