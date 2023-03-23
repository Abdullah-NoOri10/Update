from django.shortcuts import render, redirect
from .models import Product, Companie, User, Category
from .forms import CreateProductForm, EditCompanyForm, EditProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.


def comps(request):
    user = request.user
    names = Companie.objects.only('name')
    catagories = Category.objects.all()[0:8]
    list_catagories = Category.objects.all()
    product = Product.objects.all()[0:8]
    context = {'names': names, 'catagories': catagories,
               'product': product, 'user': user, 'list_catagories': list_catagories}
    return render(request, 'home.html', context)


def profile(request, pk):
    company = Companie.objects.get(id=pk)
    products = company.product_set.all()
    context = {'company': company, 'products': products}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def create_product(request):
    form = CreateProductForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        cat = request.POST.get('category')
        category = Category.objects.get(id=cat)
        product = Product.objects.create(
            name=name,
            price=price,
            category=category,
            distributor=request.user.companie,

        )
        return redirect('superuser')

    context = {'form': form}
    return render(request, 'create-product.html', context)


def login(request):
    if request.user.is_authenticated == True:
        if request.user.is_superuser == True:
            return redirect('superuser')
        else:
            return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login_user(request, user)
                return redirect('home')
            else:
                return redirect('error')

    context = {}
    return render(request, 'login.html', context)


def error_page(request):
    context = {}
    return render(request, 'error.html', context)


def sign_out(request):
    logout(request)
    context = {}
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login_user(request, user)
        return redirect('home')

    context = {}
    return render(request, 'sign_up.html', context)


def product(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    product = Product.objects.filter(Q(name__icontains=q) |
                                     Q(category__name__icontains=q))
    context = {'product': product}
    return render(request, 'product.html', context)


def company(request):
    if request.user.is_superuser != True:
        return redirect('home')
    else:
        user = request.user
        company = user.companie
        products = company.product_set.all()
    context = {'user': user, 'company': company, 'products': products}
    return render(request, 'company.html', context)


def create_company(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        user.is_superuser = True
        company_name = request.POST.get('company_name')
        company_location = request.POST.get('location')
        company_description = request.POST.get('company_description')
        Companie.objects.create(
            user=user,
            name=company_name,
            location=company_location,
            description=company_description,
            active=True
        )
        login_user(request, user)
        return redirect('superuser')
    context = {}
    return render(request, 'create-company.html', context)


def edit_company(request):
    user = request.user
    if user.is_superuser == False:
        return redirect('home')
    else:
        user = request.user
        company = user.companie
        form = EditCompanyForm(instance=company)
        if request.method == 'POST':
            form = EditCompanyForm(
                request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()
            return redirect('superuser')
        context = {'form': form}
        return render(request, 'edit-company.html', context)


def edit_products(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    user = request.user
    company = user.companie
    product = company.product_set.filter(Q(name__icontains=q))
    context = {'product': product}
    return render(request, 'edit-products.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('edit-products')


def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    form = EditProductForm(instance=product)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('superuser')
    context = {'form': form}
    return render(request, 'edit-product.html', context)


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        # message = render_to_string('mail.html', ctx)

        template = render_to_string('mail.html', {'name': name, 'message':message, 'email':email})

        # send_mail(
        #     # name,# subject
        #     message,# messag
        #     subject,# subject
        #     ['abdullahwa786@gmail.com'],# to email
        #     [email],# from email
            
            
        #     fail_silently=False, html_message=message
        # )


        send_mail( subject, template, settings.EMAIL_HOST_USER , ['noori.abdullah528@gmail.com'], fail_silently=False)


        return render(request, 'contact.html',)

    else:

        return render(request, 'contact.html', {})



def about(request):
    return render(request, 'about.html',)