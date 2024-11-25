from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime
from .models import PartnerRequest, TrialRequest, Subscription
from .forms import TrialForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def partnership(request):
    return render(request, 'partnership.html')


def partner_request(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        contact_name = request.POST.get("contact_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Ma'lumotlarni bazaga saqlash (agar kerak bo'lsa)
        PartnerRequest.objects.create(
            company_name=company_name,
            contact_name=contact_name,
            email=email,
            phone=phone,
            message=message
        )

        # Admin emailiga xabar yuborish (ixtiyoriy)
        send_mail(
            subject=f"New Partnership Request from {company_name}",
            message=f"Company Name: {company_name}\nContact Name: {contact_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            from_email='no-reply@testifyhub.com',  # O'zingizning email manzilingiz
            recipient_list=['admin@testifyhub.com'],  # Administrator email manzili
            fail_silently=False,
        )

        # Foydalanuvchiga xabar
        messages.success(request, "Thank you for your partnership request! We will get back to you soon.")

        return redirect("partnership")  # Muvaffaqiyatli bo'lsa, partnership sahifasiga yo'naltiriladi

    return render(request, "partnership.html")


def support(request):
    return render(request, 'support.html')


def support_contact(request):
    if request.method == 'POST':
        # POST ma'lumotlarni olish
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Ma'lumotni qayta ishlash yoki saqlash
        # Masalan, ma'lumotlarni email orqali yuborish yoki bazaga saqlash

        return HttpResponse("Thank you for contacting support. We will get back to you soon.")

    # Agar GET bo'lsa, support_contact.html sahifasini ko'rsatamiz
    return render(request, 'support_contact.html')


def pricing(request):
    return render(request, 'pricing.html')


# def subscribe(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         description = request.POST['description']
#         plan = request.POST['plan']
#
#         # Adminga subscribe ma'lumotini yuborish (imkoniyat bo'lsa email orqali)
#         send_mail(
#             'Yangi Subscribe!',
#             f'Ism: {first_name}\nFamiliya: {last_name}\nEmail: {email}\nTelefon: {phone}\nTa\'rif: {plan}\nIzoh: {description}',
#             'from@example.com',
#             ['admin@example.com']
#         )
#         return redirect('pricing')


def some_view(request):
    return render(request, 'some_template.html', {'year': datetime.now().year})


def watch_demo_view(request):
    return render(request, 'watch-demo.html')


def try_for_14_view(request):
    if request.method == "POST":
        form = TrialForm(request.POST)
        if form.is_valid():
            trial_request = form.save()
            return redirect('trial_success')
    else:
        form = TrialForm()

    return render(request, 'try-for-14-days.html', {'form': form})


def trial_success(request):
    return render(request, 'trial_success.html')


def subscribe(request):
    if request.method == 'POST':
        plan = request.POST.get('plan')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        # Ma'lumotlarni saqlash
        subscription = Subscription.objects.create(
            plan=plan,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            description=description
        )
        messages.success(request, f"{plan} rejasi uchun muvaffaqiyatli obuna bo'ldingiz!")
        return redirect('pricing')  # Pricing sahifasiga qayta yo'naltirish

    return render(request, 'pricing.html')  # Shaklni yana ko'rsatish (GET so'rovlari uchun)
