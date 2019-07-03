from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    ''' თუ ჩვენ ვიღებთ პოსტ მოთხოვნას,
     მაშინ ის ინახავს მომხმარებლის შექმნის ფორმას ამ პოსტის მონაცემებით,
     მაგრამ ნებისმიერ სხვა მოთხოვნით, უბრალოდ ცარიელი ფორმა იქნება და პოსტი  '''

    if request.method == 'POST': # ეს ვერ გავიგე რას აკეთებს
        form = UserRegisterForm(request.POST) # 
        if form.is_valid(): # თუ არის True
            form.save() # ბაზაში ამახსოვრებ რეგისტრირებულ მომხმარებელს
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your Account has been created! you are able to Log In !') # გამოაქვს შეტყობინება რეგისტრაციის შესახებ
            return redirect('login') # აბრუნებს მთავარ გვერდძე
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')