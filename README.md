# 🎓 Student Internship Management Portal

A full-stack **Django web application** that allows students to explore and apply for internships, while enabling admins to manage internships and applications through a secure admin panel.  
The application is deployed on **AWS EC2** with a production-ready setup using **Gunicorn + Nginx**.

---

## 🌐 Live Demo
 
[**🚀 View Live App**](http://3.26.131.158/)

> *(Hosted on AWS EC2 — may be paused when not in use)*

---

## 🚀 Features

### 👨‍🎓 Student Side

- View available internships dynamically from the database  
- Apply for internships by submitting:
  - Name  
  - Email  
  - Address  
  - Resume upload (PDF)  
- Clean and responsive user interface  
- Displays the **applied internship name** on the success page  
- **Auto-redirect** after successful application submission  

### 🧑‍💼 Admin Side

- Add, update, and delete internship postings  
- View all student applications  
- Download uploaded resumes  
- Manage data securely using **Django Admin**  

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **ORM:** Django ORM  
- **Server:** Gunicorn  
- **Reverse Proxy:** Nginx  
- **Deployment:** AWS EC2 (Ubuntu)  
- **Version Control:** Git & GitHub  

---

## 📸 Screenshots

### 🏠 Internship Listings Page

![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS1.jpg)
![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS2.jpg)
![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/SS3.jpg)
![Internship Listings](https://github.com/Prince1587/Student-Internship-Management-Portal/blob/main/Screenshot%202025-12-18%20202916.jpg)

---

## ⚙️ Installation & Setup (Local)

```bash
git clone https://github.com/Prince1587/Student-Internship-Management-Portal.git
cd Student_internship_portal

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
