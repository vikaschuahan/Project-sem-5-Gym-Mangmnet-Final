from django.shortcuts import render, redirect, get_object_or_404 # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponseRedirect # pyright: ignore[reportMissingModuleSource]
from django.contrib import messages # pyright: ignore[reportMissingModuleSource] # pyright: ignore[reportMissingModuleSource]

from django.contrib.auth.models import User # pyright: ignore[reportMissingModuleSource]
from django.contrib.auth import authenticate, logout, login # pyright: ignore[reportMissingModuleSource]
from .models import *
from django.shortcuts import render, redirect # pyright: ignore[reportMissingModuleSource]
from django.contrib.auth import authenticate, login # pyright: ignore[reportMissingModuleSource]

def index_view(request):
    # Simple index view. You can add context as needed.
    return render(request, 'index.html')

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
# Create your views here.


def Home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('home')
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)
def register_view(request):
    if request.method == 'POST':
        # Process registration form data
        # ... (add user creation logic here)
        return redirect('login')  # Redirect to login after registration
    else:
        return render(request, 'register.html')
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        # Here you can add logic:
        # 1. Check if email exists in your User model
        # 2. Generate reset link / token
        # 3. Send password reset email

        # For now, just show a success message
        messages.success(request, f"Password reset link sent to {email}")
    
    # Corrected template name
    return render(request, "forgot_passwod.html")
def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST.get('name', '').strip()
        c = request.POST.get('contact', '').strip()
        e = request.POST.get('emailid', '').strip()
        age = request.POST.get('age', '0').strip()
        g = request.POST.get('gender', '').strip()
        # New fields from the form
        branch = request.POST.get('branch', '').strip()
        enquiry_type = request.POST.get('enquiry_type', '').strip()
        contact_date = request.POST.get('contact_date', '').strip()  # maps to preferred_contact_date
        additional_info = request.POST.get('additional_info', '').strip()
        status = request.POST.get('status', 'Pending').strip()
        try:
            Enquiry.objects.create(
                name=n,
                contact=c,
                emailid=e,
                age=int(age) if age else 0,
                gender=g,
                branch=branch,
                enquiry_type=enquiry_type,
                preferred_contact_date=contact_date if contact_date else None,
                additional_info=additional_info
            )
            error = "no"
        except Exception as ex:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)
def Delete_Enquiry(request,pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')

def Edit_Enquiry(request, pid):
    enquiry = get_object_or_404(Enquiry, id=pid)
    if request.method == 'POST':
        enquiry.name = request.POST.get('name', enquiry.name).strip()
        enquiry.contact = request.POST.get('contact', enquiry.contact).strip()
        enquiry.emailid = request.POST.get('emailid', enquiry.emailid).strip()
        age = request.POST.get('age', '')
        try:
            if age != '':
                enquiry.age = int(age)
        except Exception:
            pass
        enquiry.gender = request.POST.get('gender', enquiry.gender).strip()
        enquiry.branch = request.POST.get('branch', enquiry.branch).strip()
        enquiry.enquiry_type = request.POST.get('enquiry_type', enquiry.enquiry_type).strip()
        contact_date = request.POST.get('contact_date', '')
        enquiry.preferred_contact_date = contact_date if contact_date else None
        enquiry.additional_info = request.POST.get('additional_info', enquiry.additional_info).strip()
        enquiry.status = request.POST.get('status', enquiry.status)
        enquiry.save()
        return redirect('view_enquiry')
    # render the Add Enquiry template but pre-filled for editing
    d = {'enq': enquiry}
    return render(request, 'add_enquiry.html', d)


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST.get('name', '').strip()
        category = request.POST.get('category', '').strip()
        quantity = request.POST.get('quantity', '1').strip()
        price = request.POST.get('price', '0').strip()
        unit = request.POST.get('unit', '').strip()
        date = request.POST.get('date', '').strip()
        condition = request.POST.get('condition', 'new').strip()
        desc = request.POST.get('desc', '').strip()
        try:
            Equipment.objects.create(
                name=n,
                category=category,
                quantity=int(quantity) if quantity else 1,
                price=float(price) if price else 0,
                unit=unit,
                date=date,
                condition=condition,
                description=desc
            )
            error = "no"
        except Exception as ex:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'view_equipment.html', d)

def Delete_Equipment(request,pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')

def Edit_Equipment(request, pid):
    equipment = get_object_or_404(Equipment, id=pid)
    if request.method == 'POST':
        equipment.name = request.POST.get('name', equipment.name).strip()
        equipment.category = request.POST.get('category', equipment.category).strip()
        try:
            equipment.quantity = int(request.POST.get('quantity', equipment.quantity))
        except Exception:
            pass
        try:
            equipment.price = float(request.POST.get('price', equipment.price))
        except Exception:
            pass
        equipment.unit = request.POST.get('unit', equipment.unit).strip()
        date = request.POST.get('date', '')
        equipment.date = date if date else equipment.date
        equipment.condition = request.POST.get('condition', equipment.condition).strip()
        equipment.description = request.POST.get('desc', equipment.description).strip()
        equipment.save()
        return redirect('view_equipment')
    # render the Add Equipment template but pre-filled for editing
    d = {'equipment': equipment}
    return render(request, 'add_equipment.html', d)

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create( name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Edit_Plan(request, pid):
    plan = get_object_or_404(Plan, id=pid)
    if request.method == 'POST':
        plan.name = request.POST.get('name', plan.name).strip()
        try:
            plan.amount = float(request.POST.get('amount', plan.amount))
        except Exception:
            pass
        try:
            plan.duration = int(request.POST.get('duration', plan.duration))
        except Exception:
            pass
        plan.save()
        return redirect('view_plan')
    # render add_plan but prefilled for editing
    d = {'plan': plan}
    return render(request, 'add_plan.html', d)

def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST.get('name', '').strip()
        c = request.POST.get('contact', '').strip()
        e = request.POST.get('emailid', '').strip()
        dob = request.POST.get('dob', '').strip()
        membership_type = request.POST.get('membership_type', 'basic').strip()
        address = request.POST.get('address', '').strip()
        emergency_contact = request.POST.get('emergency_contact', '').strip()
        medical_conditions = request.POST.get('medical_conditions', '').strip()
        joindate = request.POST.get('joindate', '').strip()
        expiredate = request.POST.get('expdate', '').strip()
        initialamount = request.POST.get('initialamount', '0').strip()
        # Age calculation from dob if not provided
        import datetime
        age = 0
        if dob:
            try:
                dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
                today = datetime.date.today()
                age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            except Exception:
                age = 0
        # Plan selection based on membership_type or default
        plan_obj = Plan.objects.filter(name=membership_type).first()
        if not plan_obj:
            # Create missing plan if not found
            plan_obj = Plan.objects.create(name=membership_type, amount=0, duration=0)
        if n and c and e and dob and membership_type and plan_obj and joindate and expiredate and initialamount:
            try:
                Member.objects.create(
                    name=n,
                    contact=c,
                    emailid=e,
                    age=age,
                    dob=dob if dob else None,
                    gender="",
                    membership_type=membership_type,
                    address=address,
                    emergency_contact=emergency_contact,
                    medical_conditions=medical_conditions,
                    plan=plan_obj,
                    joindate=joindate,
                    expiredate=expiredate,
                    initialamount=float(initialamount) if initialamount else 0
                )
                error = "no"
            except Exception as ex:
                import traceback
                print("Member creation error:", ex)
                traceback.print_exc()
                error = "yes"
        else:
            error = "yes"
    d = {'error': error, 'plan': plan1}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    # compute a safe status and notes for each member to avoid template errors
    import datetime
    today = datetime.date.today()
    # attach computed attributes to each member instance in memory
    for m in member:
        try:
            m.status = "Active" if m.expiredate and m.expiredate >= today else "Inactive"
        except Exception:
            m.status = "Inactive"
        # fallback for notes field (templates reference i.notes)
        if not hasattr(m, 'notes'):
            m.notes = ""
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request,pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')

def Edit_Member(request, pid):
    # use get_object_or_404 to return 404 instead of causing a server error
    member = get_object_or_404(Member, id=pid)
    plan1 = Plan.objects.all()
    if request.method == 'POST':
        member.name = request.POST.get('name', member.name).strip()
        member.contact = request.POST.get('contact', member.contact).strip()
        member.emailid = request.POST.get('emailid', member.emailid).strip()
        dob = request.POST.get('dob', '')
        if dob:
            member.dob = dob
            # recalc age
            import datetime
            try:
                dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
                today = datetime.date.today()
                member.age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            except Exception:
                pass
        member.membership_type = request.POST.get('membership_type', member.membership_type).strip()
        plan_id = request.POST.get('plan')
        if plan_id:
            try:
                plan_obj = Plan.objects.get(id=int(plan_id))
                member.plan = plan_obj
            except Exception:
                pass
        member.address = request.POST.get('address', member.address).strip()
        member.emergency_contact = request.POST.get('emergency_contact', member.emergency_contact).strip()
        member.medical_conditions = request.POST.get('medical_conditions', member.medical_conditions).strip()
        joindate = request.POST.get('joindate', '')
        if joindate:
            member.joindate = joindate
        expiredate = request.POST.get('expdate', '')
        if expiredate:
            member.expiredate = expiredate
        try:
            member.initialamount = float(request.POST.get('initialamount', member.initialamount))
        except Exception:
            pass
        member.save()
        return redirect('view_member')
    # render the add member template pre-filled for editing
    d = {'member': member, 'plan': plan1}
    return render(request, 'add_member.html', d)