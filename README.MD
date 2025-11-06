# 🏋️ Gym Management System - Django Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Project Overview

**Gym Management System** is a comprehensive web-based application built with Django that streamlines gym operations and member management. This powerful system helps gym owners and staff manage memberships, equipment, member enquiries, and workout plans efficiently.

### ✨ Key Features

🎯 **Member Management**
- Complete member registration with personal details
- Track member demographics (age, gender, contact info)
- Emergency contact information
- Member address and DOB tracking
- Profile management system

💪 **Equipment Tracking**
- Equipment inventory management
- Category-based organization
- Condition monitoring
- Purchase date tracking
- Maintenance scheduling

📝 **Enquiry Management**
- Handle potential member enquiries
- Track follow-ups and conversions
- Branch-wise enquiry management
- Additional notes and comments

💳 **Plan Management**
- Create and manage membership plans
- Flexible pricing structures
- Duration-based plans
- Custom plan creation

🔐 **User Authentication**
- Secure login/logout system
- Password recovery functionality
- User registration
- Admin dashboard access

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 📦 Installation

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/vikaschuahan/Gym-MAnagement-Project-Using-Django.git
cd "Project sem-5 Gym Mangmnet Final"
cd GMS
```

2️⃣ **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install Dependencies**
```bash
pip install django
pip install pillow  # for image handling
```

---

## 🛠️ Database Setup & Commands

### 🗄️ Database Migrations

**Make Migrations** (Create migration files based on model changes)
```bash
python manage.py makemigrations
```

**Apply Migrations** (Apply changes to database)
```bash
python manage.py migrate
```

**Show Migrations** (Check migration status)
```bash
python manage.py showmigrations
```

---

## 👤 User Management

### Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts:
- Username: `admin` (or your choice)
- Email: `your-email@example.com`
- Password: `********` (enter securely)

### Change User Password
```bash
python manage.py changepassword <username>
```

---

## 🖥️ Running the Application

### Start Development Server
```bash
python manage.py runserver
```
🌐 Access the application at: `http://127.0.0.1:8000/`

### Run on Custom Port
```bash
python manage.py runserver 8080
```

### Run on All Network Interfaces
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 📊 Admin Panel

Access the Django admin panel at: `http://127.0.0.1:8000/admin/`

**Default Admin Features:**
- ✅ Manage members, enquiries, equipment, and plans
- 📈 View database statistics
- 🔧 Configure system settings
- 👥 Manage user accounts

---

## 🎨 Project Structure

```
GMS/
├── 📁 GMS/                    # Project settings
│   ├── settings.py            # Configuration
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI config
├── 📁 gym/                    # Main application
│   ├── models.py              # Database models
│   ├── views.py               # Business logic
│   ├── admin.py               # Admin configurations
│   ├── 📁 templates/          # HTML templates
│   ├── 📁 static/             # CSS, JS, Images
│   └── 📁 migrations/         # Database migrations
├── manage.py                  # Django management script
└── db.sqlite3                 # SQLite database
```

---

## 🔧 Useful Django Commands

### 🧹 Shell & Database

**Open Django Shell**
```bash
python manage.py shell
```

**Database Shell**
```bash
python manage.py dbshell
```

**Flush Database** (⚠️ Deletes all data)
```bash
python manage.py flush
```

### 📝 Development

**Check for Issues**
```bash
python manage.py check
```

**Collect Static Files**
```bash
python manage.py collectstatic
```

**Create New App**
```bash
python manage.py startapp <app_name>
```

---

## 🎯 Database Models

### 👤 Member Model
- Personal information (name, age, gender, DOB)
- Contact details (phone, email, emergency contact)
- Address information
- Membership plan reference

### 💼 Equipment Model
- Equipment name and category
- Purchase date and cost
- Condition status
- Quantity tracking

### 📋 Enquiry Model
- Prospect information
- Enquiry date and source
- Branch information
- Follow-up notes

### 💳 Plan Model
- Plan name and description
- Duration and pricing
- Plan features

---

## 🌟 Features in Detail

### 🔐 Authentication System
- Secure user registration and login
- Password reset via email
- Session management
- Role-based access control

### 📱 Responsive Design
- Mobile-friendly interface
- Bootstrap-based UI
- Clean and modern design
- Font Awesome icons

### 🎨 Frontend Technologies
- **Bootstrap** - Responsive framework
- **jQuery** - JavaScript library
- **Font Awesome** - Icon toolkit
- **PrettyPhoto** - Lightbox plugin
- **WOW.js** - Animation library

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Delete database and start fresh
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8080
```

---

## 📸 Screenshots

*Add screenshots of your application here*

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Developer

**Vikas Chauhan**
- GitHub: [@vikaschuahan](https://github.com/vikaschuahan)
- Project Link: [Gym Management System](https://github.com/vikaschuahan/Gym-MAnagement-Project-Using-Django.git)

---

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- All contributors and supporters

---

## 📞 Support

For support, email your-email@example.com or open an issue in the GitHub repository.

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ and Django**

</div>

---

## 🔄 Quick Start Cheat Sheet

```bash
# 1. Clone and setup
git clone https://github.com/vikaschuahan/Gym-MAnagement-Project-Using-Django.git
cd "Project sem-5 Gym Mangmnet Final/GMS"
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install django pillow

# 3. Database setup
python manage.py migrate
python manage.py createsuperuser

# 4. Run server
python manage.py runserver

# 5. Access
# Frontend: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

**Last Updated:** November 2025 🚀