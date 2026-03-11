import os
import re

os.chdir(r"d:\Sem-6\GymManagmentSystem\gym\templates")

files = os.listdir(".")
for f in files:
    if not (f.startswith("add_") or f.startswith("edit_") or f.startswith("view_") or f == "attendance.html"):
        continue
    
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
        original_content = content
    
    # Remove custom body injection
    content = re.sub(r'body\s*\{\s*\n?\s*background-color:\s*#020617\s*!important;[\s\S]*?\}', '', content)
    
    content = content.replace('background: rgba(15, 23, 42, 0.85)', 'background: #ffffff')
    content = content.replace('background: rgba(15, 23, 42, 0.95)', 'background: #ffffff')
    content = content.replace('border: 1px solid rgba(255, 255, 255, 0.05)', 'border: 1px solid #e2e8f0')
    content = content.replace('border-bottom: 1px solid rgba(255,255,255,0.05)', 'border-bottom: 1px solid #e2e8f0')
    
    content = content.replace('color: #f8fafc', 'color: #0f172a')
    content = content.replace('color:#f8fafc', 'color:#0f172a')
    content = content.replace('color: #e2e8f0', 'color: #334155')
    content = content.replace('color:#e2e8f0', 'color:#334155')
    content = content.replace('color: #94a3b8', 'color: #64748b')
    content = content.replace('color:#94a3b8', 'color:#64748b')
    
    content = content.replace('background: rgba(255, 255, 255, 0.02)', 'background: #f8fafc')
    content = content.replace('background: rgba(255,255,255,0.02)', 'background: #f8fafc')
    content = content.replace('border: 1px solid rgba(255, 255, 255, 0.08)', 'border: 1px solid #cbd5e1')
    content = content.replace('border: 1px solid rgba(255,255,255,0.1)', 'border: 1px solid #cbd5e1')
    
    # Select options
    content = content.replace('background: #0f172a', 'background: #ffffff')
    
    # Table headers and views
    content = content.replace('background: rgba(255, 255, 255, 0.02) !important;', 'background: #f8fafc !important;')
    content = content.replace('border-bottom: 2px solid rgba(255, 255, 255, 0.05)', 'border-bottom: 2px solid #e2e8f0')
    content = content.replace('border-bottom: 1px solid rgba(255, 255, 255, 0.05)', 'border-bottom: 1px solid #e2e8f0')
    content = content.replace('rgba(255,255,255,0.03)', '#f1f5f9')
    content = content.replace('rgba(255,255,255,0.05)', '#f1f5f9')
    
    # Badges
    content = content.replace('rgba(59,130,246,0.1)', '#eff6ff')
    content = content.replace('rgba(59,130,246,0.2)', '#bfdbfe')
    content = content.replace('rgba(239,68,68,0.1)', '#fef2f2')
    content = content.replace('rgba(239,68,68,0.2)', '#fecaca')
    
    # Specific adjustments for view_attendance & attendance
    content = content.replace('--card-bg: #1a2332', '--card-bg: #ffffff')
    content = content.replace('--card-border: #2a3a4a', '--card-border: #e2e8f0')
    content = content.replace('background: #111b23', 'background: #f8fafc')
    content = content.replace('background: #1a2332', 'background: #ffffff')
    content = content.replace('color: #cdd9e5', 'color: #0f172a')
    content = content.replace('color: #8899aa', 'color: #64748b')
    content = content.replace('border-color: #3a4a5a', 'border-color: #cbd5e1')
    content = content.replace('background: #0d1b2a', 'background: #ffffff')
    
    if original_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated {f}")
