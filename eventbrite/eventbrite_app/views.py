from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Coordinator,Proposal,Event,SubCoordinator,SubEvent,Volunteer,Participant,Payment,Notification,Memories
from .forms import VolunteerForm,ParticipantForm,CustomUserForm,AudienceForm,PaymentForm
from .models import Audience,Participant,Volunteer,Pass

def home(request):
    return render(request,'home/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'eventbrite/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('dashboard')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            print("Registration Successfull!!!")
            return redirect('dashboard')
    else:
        form = CustomUserForm()
    return render(request, 'register/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'eventbrite/dashboard.html')

@login_required(login_url='login')
def events(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,'eventbrite/events.html',context)

@login_required(login_url='login')
def event_data(request,pid):
    event=Event.objects.get(pk=pid)
    subevents=SubEvent.objects.all().filter(event=event.id)
    context={
        'event':event,
        'subevents':subevents,
    }
    return render(request,'eventbrite/event_data.html',context)

@login_required(login_url='login')
def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VolunteerForm()
    return render(request, 'eventbrite/volunteer.html', {'form': form})

@login_required(login_url='login')
def participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ParticipantForm()
    return render(request, 'eventbrite/participant.html', {'form': form})

@login_required(login_url='login')
def audience(request):
    if request.method == 'POST':
        form = AudienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AudienceForm()
    return render(request, 'eventbrite/audience.html', {'form': form})

@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            pay = Payment(
                event=form.cleaned_data['event'],
                paymentRecieptImage=form.cleaned_data['paymentRecieptImage'],
                recieptNumber=form.cleaned_data['recieptNumber'],
                user=request.user,
                name=form.cleaned_data['name'],
                branch=form.cleaned_data['branch'],
                semester=form.cleaned_data['semester'],
                rollNumber=form.cleaned_data['rollNumber'],
                erp=form.cleaned_data['erp'],
                whatsAppNumber=form.cleaned_data['whatsAppNumber'],
                mobileNumber=form.cleaned_data['mobileNumber']
            )
            pay.save()
            return redirect('dashboard')
    else:
        form = PaymentForm()
    return render(request, 'eventbrite/payment.html', {'form': form})

@login_required(login_url='login')
def report(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,'eventbrite/report.html',context)

@login_required(login_url='login')
def profile(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,'eventbrite/profile.html',context)

@login_required(login_url='login')
def notification(request):
    notification=Notification.objects.order_by('-id')[:10][::-1]

    context={
        'notifications':notification
    }
    return render(request,'eventbrite/notification.html',context)

def pdf_generator(event_name,event_date,cname,branch,erp,students,participants,volunteer,subEventsList,budget):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
    from reportlab.lib import colors

    # Create a new PDF object
    pdf = SimpleDocTemplate("C://Users//Shraddha//Documents//eventbrite//eventbrite//eventbrite_app//static//eventreport.pdf", pagesize=letter)

    # Define the styles for the document
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    subtitle_style = styles["Heading2"]
    text_style = styles["Normal"]

    # Define the data for the event report
    title = event_name
    event_name = event_name
    event_date = event_date
    coordinator = [["Coordinator Name", "Branch", "ERP Number"], [cname,branch,erp]]
    persons = [["Total No. Of Students", "Total No. Of Participants", "Total No. Of Volunteer"], [students,participants,volunteer]]
    subEvents = [["Sub Event", "Total Budget","Utilise Budget", "Balance Budget"]]
    for x in subEventsList:
        subEvents.append(x)
    b = [["Budget", "Utilise Budget", "Balance Budget"],budget]
    summary = "The goal of the event is to help new students feel welcome and supported as they begin their college journey. It can be a great opportunity for new students to make new friends and connections, get involved in campus life, and learn about the resources available to them."

    # Add content to the PDF

    story = []
    logo = Image("C://Users//Shraddha//Documents//eventbrite//eventbrite//eventbrite_app//ltcoe.png", width=2*inch, height=2*inch)  # Replace "logo.png" with your logo file name
    story.append(logo)
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Event Details", subtitle_style))
    story.append(Paragraph(f"Event Name: {event_name}", text_style))
    story.append(Paragraph(f"Event Date: {event_date}", text_style))


    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Coordinator", subtitle_style))
    table = Table(coordinator)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Audience", subtitle_style))
    table = Table(persons)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Sub Events List", subtitle_style))
    table = Table(subEvents)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Budget", subtitle_style))
    table = Table(b)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    

    story.append(Paragraph("Summary", subtitle_style))
    story.append(Paragraph(summary, text_style))

    # Build the PDF document
    pdf.build(story)
    print("PDF Generated Successfully!")

@login_required(login_url='login')
def generatereport(request,pid):
    event=Event.objects.get(id=pid)
    coordinator=Coordinator.objects.get(name=event.coordinator)
    subevents=SubEvent.objects.filter(event=pid)
    students=Audience.objects.count()
    participants=Participant.objects.count()
    volunteer=Volunteer.objects.count()
    subEventsList=[]
    budget=[]
    totalBudgetSum=0
    utiliseBudgetSum=0
    balanceBudgetSum=0
    for x in subevents:
            tempList=[]
            tempList.append(x.name)
            tempList.append(x.totalBudget)
            tempList.append(x.utiliseBudget)
            tempList.append(x.balanceBudget)
            subEventsList.append(tempList)
            totalBudgetSum+=int(x.totalBudget)
            utiliseBudgetSum+=int(x.utiliseBudget)
            balanceBudgetSum+=int(x.balanceBudget)
    budget.append(totalBudgetSum)
    budget.append(utiliseBudgetSum)
    budget.append(balanceBudgetSum)

    print('Calling PDF Generation')
    pdf_generator(event.name,event.eventDate,coordinator.name,coordinator.branch,coordinator.erp,students,participants,volunteer,subEventsList,budget)
    print('Ending PDF Generation')
    context={
        'event':event
    }
    return render(request,'eventbrite/downloadreport.html',context)

@login_required(login_url='login')
def generate_pass(request, event_id):
    import uuid
    event = Event.objects.get(id=event_id)
    pass_uuid = uuid.uuid4()
    try:
        passes = Pass.objects.get(name=request.user.username, event=event)
    except Pass.DoesNotExist:
        passes = Pass(name=request.user.username, event=event, date=event.eventDate, uuid=pass_uuid)
        passes.save()
    try:
        pay = Payment.objects.get(user=request.user, event=event)
    except Payment.DoesNotExist:
        pay = None
    return render(request, 'eventbrite/pass.html', {'pass': passes, 'payment': pay})

@login_required(login_url='login')
def generate_qr(request):
    import qrcode
    from django.http import HttpResponse
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    pay=Payment.objects.get(user=request.user)
    # qr.add_data('Dosti ka rishta koi rang nahi hota, Par jab saath hote hain toh zindagi roshan hoti hai, Dosti mein dard bhi ho toh sukoon milta hai, Kunki ek dost ke saath har mushkil aasaan hoti hai.')
    # qr.add_data('Dosti ki gehrai se khud ko samajhne lage hain, Har rishta humari zindagi ke imtihaan banne lage hain, Dosti ki qadar dil mein basa ke rakhna, Kyunki yeh rishta har mod par saath nibhane wala hai.')
    qr.add_data("username :- "+pay.user.username +" erp number :- "+str(pay.erp)+" event :- "+str(pay.event))
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
    img.save(response, 'PNG')
    return response

