from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/registration/signup.html"


@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            profile.user = user
            profile.save()
            user.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return render(request, 'registration/signup_done.html', {'new_user': user})
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'registration/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form})