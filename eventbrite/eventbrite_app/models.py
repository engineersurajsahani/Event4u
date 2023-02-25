from django.db import models

# Create your models here.

BRANCH = [
    ('Computer', 'Computer'),
    ('AIML', 'AIML'),
    ('Data Science', 'Data Science'),
    ('IOT', 'IOT')
]

SEMESTER = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8')
]

STATUS = [
    ('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Completed', 'Completed')
]

class Coordinator(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Proposal(models.Model):
    coordinator=models.ForeignKey(Coordinator,on_delete=models.CASCADE)
    description=models.TextField(null=False,blank=False)
    feeApplicableForPerStudent=models.PositiveIntegerField(null=False,blank=False)
    fundRecieveFromCollege=models.PositiveIntegerField(null=False,blank=False)
    hodApproval=models.BooleanField(default=False,null=False,blank=False)
    adminApproval=models.BooleanField(default=False,null=False,blank=False)
    status=models.CharField(max_length=50,choices=STATUS,null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coordinator

class Event(models.Model):
    coordinator=models.ForeignKey(Coordinator,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    image=models.ImageField(upload_to='events')
    status=models.CharField(max_length=50,choices=STATUS,null=False,blank=False)
    upi=models.CharField(max_length=100,blank=True,null=True)
    totalMoney=models.PositiveIntegerField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    eventDate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubCoordinator(models.Model):
    coordinator=models.ForeignKey(Coordinator,on_delete=models.CASCADE,null=False,blank=False)
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubEvent(models.Model):
    coordinator=models.ForeignKey(Coordinator,on_delete=models.CASCADE,null=False,blank=False)
    subcoordinator=models.ForeignKey(SubCoordinator,on_delete=models.CASCADE,null=False,blank=False)
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    image=models.ImageField(upload_to='subevents')
    totalBudget=models.PositiveIntegerField(null=True,blank=True)
    utiliseBudget=models.PositiveIntegerField(null=True,blank=True)
    balanceBudget=models.PositiveIntegerField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    eventDate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    subevent=models.ForeignKey(SubEvent,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    isVolunteer=models.BooleanField(default=False,null=False,blank=False)
    work=models.TextField(null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    subevent=models.ForeignKey(SubEvent,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    isParticipant=models.BooleanField(default=False,null=False,blank=False)
    interest=models.TextField(null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Audience(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    isAudience=models.BooleanField(default=False,null=False,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Payment(models.Model):
    from django.contrib.auth.models import User
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    paymentRecieptImage=models.ImageField(upload_to='payment',null=False,blank=False)
    recieptNumber=models.CharField(max_length=10,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=False,blank=False)
    branch=models.CharField(max_length=50,choices=BRANCH)
    semester=models.CharField(max_length=50,choices=SEMESTER)
    rollNumber=models.PositiveIntegerField(null=False,blank=False)
    erp=models.PositiveBigIntegerField(null=False,blank=False)
    whatsAppNumber=models.CharField(max_length=10,null=False,blank=False)
    mobileNumber=models.CharField(max_length=10,null=False,blank=False)
    coordinatorCheck=models.BooleanField(default=False,null=False,blank=False)

    def __str__(self):
        return self.name

class Notification(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    description=models.TextField(null=False,blank=False)

    def __str__(self):
        return self.event

class Memories(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=False,blank=False)
    subevent=models.ForeignKey(SubEvent,on_delete=models.CASCADE,null=False,blank=False)
    image=models.ImageField(upload_to='memories')
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event

class Pass(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    uuid = models.UUIDField(unique=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    