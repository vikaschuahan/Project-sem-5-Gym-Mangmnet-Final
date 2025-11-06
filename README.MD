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
Project sem-5 Gym Mangmnet Final/
│
├── 📁 GMS/                              # Django Project Configuration
│   ├── __init__.py
│   ├── asgi.py                          # ASGI configuration
│   ├── settings.py                      # Django settings & configuration
│   ├── urls.py                          # Root URL routing
│   ├── wsgi.py                          # WSGI configuration
│   └── 📁 __pycache__/                  # Python cache files
│
├── 📁 gym/                              # Main Application
│   ├── __init__.py
│   ├── admin.py                         # Admin panel configurations
│   ├── apps.py                          # App configuration
│   ├── models.py                        # Database models (Member, Equipment, etc.)
│   ├── tests.py                         # Unit tests
│   ├── views.py                         # View functions & business logic
│   ├── 📁 __pycache__/                  # Python cache files
│   │
│   ├── 📁 migrations/                   # Database Migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py              # Initial migration
│   │   ├── 0002_auto_20200907_1813.py
│   │   ├── 0003_member_gender.py
│   │   ├── 0004_auto_20200911_0721.py
│   │   ├── 0005_userlogin.py
│   │   ├── 0006_delete_userlogin.py
│   │   ├── 0007_remove_member_initialamount_alter_enquiry_age_and_more.py
│   │   ├── 0008_alter_enquiry_id_alter_equipment_id_alter_member_id_and_more.py
│   │   ├── 0009_equipment_category_equipment_condition_and_more.py
│   │   ├── 0010_member_address_member_dob_member_emergency_contact_and_more.py
│   │   ├── 0011_enquiry_additional_info_enquiry_branch_and_more.py
│   │   └── 📁 __pycache__/
│   │
│   ├── 📁 static/                       # Static Files (CSS, JS, Images)
│   │   ├── 📁 css/                      # Stylesheets
│   │   │   ├── animate.min.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── font-awesome.css
│   │   │   ├── font-awesome.min.css
│   │   │   ├── main.css
│   │   │   ├── prettyphoto.css
│   │   │   ├── style.css
│   │   │   └── styles.css
│   │   │
│   │   ├── 📁 images/                   # Images & Assets
│   │   │   ├── a111.jfif
│   │   │   ├── 📁 banner/               # Banner images
│   │   │   ├── 📁 ico/                  # Icons
│   │   │   ├── 📁 portfolio/            # Portfolio images
│   │   │   ├── 📁 prettyPhoto/          # Lightbox themes
│   │   │   │   ├── 📁 dark_rounded/
│   │   │   │   ├── 📁 dark_square/
│   │   │   │   ├── 📁 default/
│   │   │   │   ├── 📁 facebook/
│   │   │   │   ├── 📁 light_rounded/
│   │   │   │   └── 📁 light_square/
│   │   │   └── 📁 team/                 # Team member images
│   │   │
│   │   └── 📁 js/                       # JavaScript Files
│   │       ├── bootstrap.min.js
│   │       ├── custom-scripts.js
│   │       ├── html5shiv.js
│   │       ├── jquery.inview.min.js
│   │       ├── jquery.isotope.min.js
│   │       ├── jquery.js
│   │       ├── jquery.prettyphoto.js
│   │       ├── mousescroll.js
│   │       ├── respond.min.js
│   │       ├── smoothscroll.js
│   │       └── wow.min.js
│   │
│   └── 📁 templates/                    # HTML Templates
│       ├── about.html                   # About page
│       ├── add_enquiry.html             # Add enquiry form
│       ├── add_equipment.html           # Add equipment form
│       ├── add_member.html              # Add member form
│       ├── add_plan.html                # Add plan form
│       ├── contact.html                 # Contact page
│       ├── edit_enquiry.html            # Edit enquiry form
│       ├── edit_equipment.html          # Edit equipment form
│       ├── edit_member.html             # Edit member form
│       ├── edit_plan.html               # Edit plan form
│       ├── footer.html                  # Footer component
│       ├── forgot_passwod.html          # Password recovery
│       ├── index.html                   # Home page
│       ├── login.html                   # Login page
│       ├── navigation.html              # Navigation bar
│       ├── register.html                # Registration page
│       ├── view_enquiry.html            # View enquiries
│       ├── view_equipment.html          # View equipment
│       ├── view_member.html             # View members
│       └── view_plan.html               # View plans
│
├── manage.py                            # Django management script
├── db.sqlite3                           # SQLite database (auto-generated)
├── README.MD                            # Project documentation
└── .gitignore                           # Git ignore rules
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
- Follow-up notes and additional info

### 💳 Plan Model
- Plan name and description
- Duration and pricing
- Plan features

---

## 📄 Available Templates

### Public Pages
- **index.html** - Landing page with gym information
- **about.html** - About the gym and services
- **contact.html** - Contact form and information

### Authentication
- **login.html** - User login
- **register.html** - New user registration
- **forgot_passwod.html** - Password recovery

### Member Management
- **add_member.html** - Add new member
- **edit_member.html** - Edit member details
- **view_member.html** - View all members

### Equipment Management
- **add_equipment.html** - Add new equipment
- **edit_equipment.html** - Edit equipment details
- **view_equipment.html** - View all equipment

### Enquiry Management
- **add_enquiry.html** - Add new enquiry
- **edit_enquiry.html** - Edit enquiry details
- **view_enquiry.html** - View all enquiries

### Plan Management
- **add_plan.html** - Add new membership plan
- **edit_plan.html** - Edit plan details
- **view_plan.html** - View all plans

### Components
- **navigation.html** - Navigation bar component
- **footer.html** - Footer component

---

## 🌟 Features in Detail

### 🔐 Authentication System
- Secure user registration and login
- Password reset functionality
- Session management
- Role-based access control

### 📱 Responsive Design
- Mobile-friendly interface
- Bootstrap framework
- Clean and modern UI
- Smooth animations with WOW.js

### 🎨 Frontend Technologies
- **Bootstrap** - Responsive CSS framework
- **jQuery** - JavaScript library
- **Font Awesome** - Icon toolkit
- **PrettyPhoto** - Lightbox plugin
- **WOW.js** - Animation library
- **Isotope** - Filter & sort layouts
- **SmoothScroll.js** - Smooth scrolling
- **Animate.css** - CSS animations

### 📊 Admin Features
- Django admin panel integration
- CRUD operations for all models
- Data filtering and searching
- Export functionality

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Delete database and start fresh
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Delete migration files (keep __init__.py)
cd gym\migrations
# Manually delete numbered migration files, keep __init__.py

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

### Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove and recreate
rmdir /s venv  # Windows
rm -rf venv    # Linux/Mac

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

pip install django pillow
```

### Migration Conflicts
```bash
# If you encounter migration conflicts
python manage.py migrate --fake-initial
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
- jQuery Team
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
cd "Project sem-5 Gym Mangmnet Final"

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install django pillow

# 4. Database setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 5. Run server
python manage.py runserver

# 6. Access
# Frontend: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

**Last Updated:** November 2025 🚀