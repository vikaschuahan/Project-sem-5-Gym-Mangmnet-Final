import os
import re

os.chdir(r"d:\Sem-6\GymManagmentSystem\gym\templates")

files = [f for f in os.listdir(".") if f.startswith("view_") and f.endswith(".html")]

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    original = content
        
    # Remove inline styling from badges so they use exactly the class definition
    content = re.sub(r'class="badge-blue"[^>]*>', 'class="badge-blue">', content)
    content = re.sub(r'class="badge-green"[^>]*>', 'class="badge-green">', content)
    content = re.sub(r'class="badge-yellow"[^>]*>', 'class="badge-yellow">', content)
    content = re.sub(r'class="badge-red"[^>]*>', 'class="badge-red">', content)
    content = re.sub(r'class="badge-gray"[^>]*>', 'class="badge-gray">', content)

    # Some old ones use `span class="plan-chip" style="..."`
    content = re.sub(r'class="plan-chip"[^>]*>', 'class="badge-blue">', content)

    # Some text color inline overrides
    content = content.replace('color:#334155;', 'color:#4f46e5;')

    if content != original:
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated badges in {f}")
        
