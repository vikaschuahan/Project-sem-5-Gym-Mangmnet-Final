import os
import re

os.chdir(r"d:\Sem-6\GymManagmentSystem\gym\templates")

files = [f for f in os.listdir(".") if f.startswith("view_") and f.endswith(".html")]

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    original = content
        
    # Remove all style blocks in view files (we will use global classes)
    content = re.sub(r'<style>[\s\S]*?</style>', '', content)
    
    # Replace inline styles for buttons
    content = re.sub(r'style="display:inline-flex;align-items:center;gap:4px;color:#60a5fa;[^"]*"', 'class="btn-action-edit"', content)
    content = re.sub(r'style="display:inline-flex;align-items:center;gap:4px;color:#f87171;[^"]*"', 'class="btn-action-delete"', content)
    
    # Replace inline styles on email/phones that make them dark instead of blue
    content = content.replace('color:#334155;', 'color:#4f46e5;')
    content = content.replace('color:#0f172a;', '')
    content = content.replace('color:#64748b;', 'color:#6b7280;')

    # Fix badges
    content = content.replace('badge-red">{{ e.status }}', 'badge-gray">{{ e.status }}')

    if content != original:
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated {f}")
        
