"""
PythonAnywhere WSGI configuration for the Gym Management System (GMS).

INSTRUCTIONS
============
1. Log in to PythonAnywhere and open the Web tab for your app.
2. Click "WSGI configuration file" to open this file in the online editor.
3. Replace the default contents with the code below (adjust the path and
   environment-variable values to match your own account).

For full deployment steps see README.MD → "Deploy to PythonAnywhere".
"""

import os
import sys

# ------------------------------------------------------------------
# 1. Add your project directory to sys.path so Python can find GMS/
# ------------------------------------------------------------------
# Replace 'yourusername' with your actual PythonAnywhere username
# and adjust the path if your repo lives in a sub-folder.
path = '/home/yourusername/Project-sem-5-Gym-Mangmnet-Final'
if path not in sys.path:
    sys.path.insert(0, path)

# ------------------------------------------------------------------
# 2. Point Django at the correct settings module
# ------------------------------------------------------------------
os.environ['DJANGO_SETTINGS_MODULE'] = 'GMS.settings'

# ------------------------------------------------------------------
# 3. Set required environment variables
#    (you can also set these in the PythonAnywhere "Environment
#     variables" panel on the Web tab instead of hard-coding here)
# ------------------------------------------------------------------
# Generate a fresh key with:
#   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
os.environ.setdefault('SECRET_KEY', 'change-me-to-a-long-random-string')

# NEVER set DEBUG=True in production
os.environ.setdefault('DEBUG', 'False')

# Replace with your actual PythonAnywhere subdomain (and any custom domain)
os.environ.setdefault('ALLOWED_HOSTS', 'yourusername.pythonanywhere.com')

# ------------------------------------------------------------------
# 4. Load the Django WSGI application
# ------------------------------------------------------------------
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
