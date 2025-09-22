#!/usr/bin/env python
import os
import sys
import django

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uoas.settings')
django.setup()

from dashboard.models import Manager
from django.contrib.auth.hashers import make_password

def reset_manager_password(username, new_password):
    """Reset a manager's password with proper hashing"""
    try:
        manager = Manager.objects.get(username=username)
        manager.password = make_password(new_password)
        manager.save()
        print(f"✅ Successfully reset password for manager: {username}")
        return True
    except Manager.DoesNotExist:
        print(f"❌ Manager with username '{username}' does not exist")
        return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        reset_manager_password(username, password)
    else:
        print("Usage: python fix_manager_password.py <username> <new_password>")
        print("Example: python fix_manager_password.py admin newpass123")
