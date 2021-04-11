from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import CreateUserForm
from .models import Product, Youtube


def index(request):
    product = Product.objects.all()
    youtuber = Youtube.objects.all()
    return render(request, 'home.html', {'product': product, 'youtuber': youtuber})


def product_detail(request, id):
    products = get_object_or_404(Product, pk=id)
    return render(request, 'product/detail.html', {'products': products})


def product_grid(request):
    context = Product.objects.all()
    return render(request, 'product/product.html', {'context': context})


def youtube_page(request):
    ctx = Youtube.objects.all()
    return render(request, 'youtube/youtube.html', {'ctx': ctx})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'account/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class Profile(UpdateView):
    model = User
    template_name = 'account/profile.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'special_user', 'is_author']

    success_url = reverse_lazy('store:profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)


