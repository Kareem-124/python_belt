from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
import bcrypt

# Page : Login Page
def index(request):
    return render(request, 'index.html')

# Process: Registration Process: Validation Included
def reg_process(request):
    # Validation Part Section
    error = User.objects.validate(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/')
    else:  # if Validation passed store the user in the db and encrypt the password
        password = request.POST['password']
        ps_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=ps_hash
        )
        messages.success(request, "User has been created Successfully!")
        return redirect('/')
    

# Process: Login Process: Validation Included
def login_process(request):
    # see if the username provided exists in the database
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = logged_user.id
            messages.success(request, "You have Successfully logged in")
            return redirect('/success')
        else:
            # if we didn't find anything in the database by searching by username or if the passwords don't match,
            messages.error(request, "Email or Password incorrect")
            return redirect('/')
    else:
        # if we didn't find anything in the database by searching by username or if the passwords don't match,
        messages.error(request, "Email or Password incorrect")
        return redirect('/')
    
# : This will clear the massages from messages (error / success) --> redirect to /success
def success_redirect_process(request):
    list(messages.get_messages(request))
    return redirect('/success')

# Page : Open The main page after the user successfully logged in, it will open ""
def success(request):
    # Create User Session
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user_object' : user
    }
    return render(request, 'success.html', context)


# Process : Logout
def logout_process(request):
    # This will clear the massages from messages (error / success)
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')

# Page : table
def table(request):
    return render(request,'table.html')


# Page : form
def form(request):
    return render(request,'form.html')
