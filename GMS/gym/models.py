from django.db import models # pyright: ignore[reportMissingModuleSource]

# Enquiry model
class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=15)  # Allow more digits for flexibility
    emailid = models.EmailField(max_length=60)  # Better validation
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=100, blank=True, default="")
    enquiry_type = models.CharField(max_length=50, blank=True, default="")
    preferred_contact_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")
    additional_info = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


# Equipment model
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10)
    date = models.DateField()  # Proper DateField
    condition = models.CharField(max_length=20, default="new")
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


# Plan model
class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days or months")

    def __str__(self):
        return self.name


# Member model
class Member(models.Model):
    
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    emailid = models.EmailField(max_length=50)
    age = models.PositiveIntegerField()
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, default="")
    membership_type = models.CharField(max_length=20, default="basic")
    address = models.CharField(max_length=200, blank=True, default="")
    emergency_contact = models.CharField(max_length=50, blank=True, default="")
    medical_conditions = models.TextField(blank=True, default="")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)  # Linked to Plan
    joindate = models.DateField()
    expiredate = models.DateField()
    initialamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
