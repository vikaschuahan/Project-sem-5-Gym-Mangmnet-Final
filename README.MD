# 🏋️ Gym Management System - Django Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Project Overview

**Gym Management System** is a comprehensive web-based application built with Django that streamlines gym operations and member management. This powerful system helps gym owners and staff manage memberships, equip ment, member enquiries, and workout plans efficiently.

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

## 🚀 Deployment

This project is ready to deploy to platforms like **Heroku**, **Railway**, or **Render**.

### ⚙️ Environment Variables

Before deploying, set the following environment variables on your hosting platform:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key (keep it secret!) | `your-random-secret-key` |
| `DEBUG` | Enable debug mode (`True` only for development) | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `mygymapp.herokuapp.com` |

> **Generate a new SECRET_KEY:**
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 🟣 Deploy to Heroku

```bash
# 1. Install Heroku CLI and log in
heroku login

# 2. Create a Heroku app
heroku create your-gym-app-name

# 3. Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG="False"
heroku config:set ALLOWED_HOSTS="your-gym-app-name.herokuapp.com"

# 4. Push and deploy
git push heroku main

# 5. Run database migrations
heroku run python manage.py migrate

# 6. Create superuser
heroku run python manage.py createsuperuser
```

### 🟦 Deploy to Railway

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) and create a new project from your GitHub repo
3. Add the environment variables (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) in the Railway dashboard
4. Railway will automatically detect the `Procfile` and deploy

### 🟩 Deploy to Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a **Web Service** from your GitHub repo
3. Set **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
4. Set **Start Command**: `gunicorn GMS.wsgi --log-file -`
5. Add environment variables in the Render dashboard

### 🐍 Deploy to PythonAnywhere

PythonAnywhere provides a free tier that is well-suited for small Django applications.
Follow the steps below to host the Gym Management System there.

---

#### Prerequisites

- A free (or paid) [PythonAnywhere](https://www.pythonanywhere.com) account
- Your code pushed to GitHub (or uploaded as a ZIP)

---

#### Step 1 – Open a Bash console on PythonAnywhere

1. Log in to PythonAnywhere.
2. Go to **Dashboard → Consoles → Bash** and start a new Bash console.

---

#### Step 2 – Clone (or upload) the repository

```bash
# Option A – clone directly from GitHub (recommended)
git clone https://github.com/vikaschuahan/Project-sem-5-Gym-Mangmnet-Final.git

# Option B – if you uploaded a ZIP via the Files tab
unzip Project-sem-5-Gym-Mangmnet-Final.zip
```

---

#### Step 3 – Create a virtual environment and install dependencies

PythonAnywhere supports Python 3.10+. Adjust the version flag if needed.

```bash
cd Project-sem-5-Gym-Mangmnet-Final

# Create a virtual environment (use the Python version you want)
python3.10 -m venv venv

# Activate it
source venv/bin/activate

# Install all required packages
pip install -r requirements.txt
```

> **Tip:** Use `python3.10` (or `python3.11`) explicitly because the default
> `python` on PythonAnywhere may point to Python 2.

---

#### Step 4 – Generate a secure SECRET_KEY

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output – you will need it in the next step.

---

#### Step 5 – Set environment variables

PythonAnywhere lets you set environment variables in the **Web tab → Environment variables** panel (recommended), or you can export them directly in the WSGI file (see Step 7).

Minimum required variables:

| Variable | Value |
|---|---|
| `SECRET_KEY` | Long random string from Step 4 |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `yourusername.pythonanywhere.com` |

---

#### Step 6 – Run database migrations and collect static files

```bash
# Apply all migrations
python manage.py migrate

# Gather static files into staticfiles/
python manage.py collectstatic --noinput

# Create the admin superuser
python manage.py createsuperuser
```

---

#### Step 7 – Create a new Web app and configure the WSGI file

1. In the PythonAnywhere **Web** tab click **"Add a new web app"**.
2. Choose **Manual configuration** (not the Django quick-start wizard).
3. Select the same Python version you used in Step 3.
4. Once the app is created, click **"WSGI configuration file"** to open it.
5. **Delete all existing content** and paste the contents of
   `pythonanywhere_wsgi.py` (provided in this repo), then update the two
   placeholders:

```python
import os
import sys

# Replace 'yourusername' with your PythonAnywhere username
path = '/home/yourusername/Project-sem-5-Gym-Mangmnet-Final'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'GMS.settings'

# Paste your generated SECRET_KEY here, or set via the Web tab panel
os.environ.setdefault('SECRET_KEY', 'your-secret-key-here')
os.environ.setdefault('DEBUG', 'False')
os.environ.setdefault('ALLOWED_HOSTS', 'yourusername.pythonanywhere.com')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. Save the file.

---

#### Step 8 – Configure the virtual environment path

In the **Web tab** under **"Virtualenv"**, enter the full path:

```
/home/yourusername/Project-sem-5-Gym-Mangmnet-Final/venv
```

---

#### Step 9 – Configure static files

In the **Web tab** under **"Static files"**:

| URL | Directory |
|---|---|
| `/static/` | `/home/yourusername/Project-sem-5-Gym-Mangmnet-Final/staticfiles` |
| `/media/` | `/home/yourusername/Project-sem-5-Gym-Mangmnet-Final/media` |

---

#### Step 10 – Reload and test

1. Click the green **"Reload"** button at the top of the Web tab.
2. Visit `https://yourusername.pythonanywhere.com/` – you should see the gym landing page.
3. Visit `https://yourusername.pythonanywhere.com/admin/` to log in to the admin panel.

---

#### 🚨 PythonAnywhere Error Handling & Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| **500 Internal Server Error** | Uncaught Python exception | Check the **Error log** in the Web tab |
| **"DisallowedHost" error** | Your domain is not in `ALLOWED_HOSTS` | Add `yourusername.pythonanywhere.com` to the `ALLOWED_HOSTS` env var |
| **Static files not loading (CSS/JS missing)** | `collectstatic` not run or wrong path | Run `python manage.py collectstatic --noinput` and verify the Static Files mapping in the Web tab |
| **"No module named 'GMS'"** | Wrong `path` in WSGI file | Make sure `path` points to the folder that *contains* `manage.py` |
| **"No module named 'django'"** | Virtual environment not activated / wrong path | Verify the **Virtualenv** path in the Web tab; re-run `pip install -r requirements.txt` inside the venv |
| **Media files (uploads) not showing** | Missing media static mapping | Add `/media/` → `…/media` in the Static Files section of the Web tab |
| **Database errors after update** | Pending migrations | Run `python manage.py migrate` in a Bash console, then reload |
| **"OperationalError: no such table"** | Migrations never ran | Run `python manage.py migrate` |
| **Reloading does not pick up code changes** | Old `.pyc` cache | Delete `__pycache__` folders (`find . -name '__pycache__' -exec rm -rf {} +`) then reload |
| **Free account "sleeping" site** | PythonAnywhere free tier limitation | Log in and click **"Run until 3 months from today"** in the Web tab, or upgrade to a paid plan |

**Reading the error logs**

PythonAnywhere provides three log files (visible in the Web tab):
- **Access log** – every HTTP request
- **Error log** – Python tracebacks and Django errors ← *start here*
- **Server log** – low-level WSGI server messages

Always check the **Error log** first when something goes wrong.

---

### 🐳 Deploy with Docker (Optional)

You can also containerise the app. Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "GMS.wsgi", "--bind", "0.0.0.0:8000", "--log-file", "-"]
```

### 📝 Post-Deployment Checklist

- [ ] Set `SECRET_KEY` to a strong, unique value
- [ ] Set `DEBUG=False`
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Run `python manage.py migrate`
- [ ] Run `python manage.py createsuperuser`
- [ ] Verify static files are served correctly

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
