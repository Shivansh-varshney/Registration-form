from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

# utility functions
def check_username(username):
    try:
        user = User.objects.get(username = username)
        return True
    
    except User.DoesNotExist:
        return False

def check_email(email):
    try:
        user = User.objects.get(email = email)
        return True
    
    except User.DoesNotExist:
        return False

# Create your views here.
@login_required(login_url='/signin')
def application(request):
    return render(request, 'application.html')

@login_required(login_url='/signin')
def bankdetail(request):
    bank_detail.objects.get_or_create(username = request.user.username)
    
    bank_instance = get_object_or_404(bank_detail, username = request.user.username)
    progress = progressreport.objects.get(username = request.user.username)
    
    if request.method == 'POST':
        bankform = BankDetailsForm(request.POST, instance=bank_instance)

        try:
            if bankform.is_valid():
                new_entry = bankform.save(commit=False)
                new_entry.username = request.user.username
                new_entry.save()
                progress.bank_detail = True
                progress.save()
                messages.success(request, 'Bank Details added Successfully!!')
                return redirect('/phase1')
        except Exception as e:
            messages.error(request, f"Error:{e}")
    else:
        bankform = BankDetailsForm(instance=bank_instance)
    return render(request, 'bank_detail.html', {'bankform':bankform,'progress':progress})

# change the user account password
@login_required(login_url='/signin')
def change(request):
    if request.method == 'POST':
       
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            try:
                user = User.objects.get(username = request.user)
                user.set_password(f'{new_password}')
                user.save()

                messages.success(request, 'Your password changed successfully!!')
                return redirect('/logout')
            
            except Exception as error:
                messages.error(request, f'Error: {error}')
                return redirect('change_password')
    
    return render(request, 'change_password.html')

@login_required(login_url='/signin')
def education(request):
    school_detail.objects.get_or_create(username = request.user.username)
    subject_mark.objects.get_or_create(username = request.user.username)
    
    school_instance = get_object_or_404(school_detail, username = request.user.username)
    subject_instance = get_object_or_404(subject_mark, username = request.user.username)
    progress = progressreport.objects.get(username = request.user.username)
    
    if request.method == "POST":
        schoolform = SchoolDetailsForm(request.POST, instance=school_instance)
        marksform = SubjectMarksForm(request.POST, instance=subject_instance)

        if schoolform.is_valid() and marksform.is_valid():
            schoolform_entry = schoolform.save(commit=False)
            marksform_entry = marksform.save(commit=False)

            schoolform_entry.username = request.user.username
            marksform_entry.username = request.user.username

            schoolform_entry.save()
            marksform_entry.save() 
            progress.education = True
            progress.save()
            messages.success(request, 'Education details added successfully!!')
            return redirect('/bank_detail')
            
    else:
        schoolform = SchoolDetailsForm(instance=school_instance)
        marksform = SubjectMarksForm(instance=subject_instance)
    return render(request, 'education.html',{'schoolform':schoolform, 'marksform': marksform,'progress':progress})

@login_required(login_url='/signin')
def familydetail(request):
    Family_detail.objects.get_or_create(username=request.user.username)
    
    family_instance = get_object_or_404(Family_detail, username = request.user.username)
    progress = progressreport.objects.get(username = request.user.username) 
    
    if request.method == 'POST':
        familyform = FamilyDetailsForm(request.POST, instance= family_instance)

        if familyform.is_valid():
            new_entry = familyform.save(commit=False)
            # Assign the current authenticated user to the user field
            new_entry.username = request.user.username
            # Now save the object with the user assigned
            new_entry.save()
            progress.family_detail = True
            progress.save()
            messages.success(request, "Family details added successfully!!")
            return redirect('/personal_detail')
    
    else:
        familyform = FamilyDetailsForm(instance= family_instance)
    return render(request, 'family_detail.html', {'familyform':familyform,'progress':progress})

def help(request):
    return render(request, 'helpdesk.html')

# home page of the site
@login_required(login_url='/signin')
def index(request):
    progressreport.objects.get_or_create(username = request.user.username)
    progress_boolean = progressreport.objects.get(username = request.user.username)
    return render(request, 'index.html',{'progress':progress_boolean})

# login to the site
def loginuser(request):

    if request.method == 'POST':
        # check whether the user credentials are valid
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.error(request, "Please fill the form.")
            return redirect('/signin')
        else:
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
            elif user is None:
                messages.error(request, "No user with such Credentials.")
                return redirect('/signin')
            
            else:
                messages.error(request, "Could not login.")
                return redirect('/signin')

    return render(request, 'signin.html')

# logout from the site
def logoutuser(request):

    logout(request)
    messages.success(request, "You have been logged out successfully. Kindly login again to continue.")
    return redirect('/signin')


# help user see and update account details 
@login_required(login_url='/signin')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            
            user = User.objects.get(username = request.user)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            if first_name != user.first_name:
                user.first_name = first_name
                user.save()

            elif last_name != user.last_name:
                user.last_name = last_name
                user.save()

            messages.success(request, 'Account Details Updated successfully.')
            return redirect('/profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
                
    return render(request, 'profile.html', {'user_form':user_form})

@login_required(login_url='/signin')
def phase1(request):
    progress_boolean = progressreport.objects.get(username = request.user.username)
    return render(request, 'phase1.html', {'progress':progress_boolean})

@login_required(login_url='/signin')
def phase2(request):
    return render(request, 'phase2.html')

@login_required(login_url='/signin')
def personaldetail(request):
    Personal_detail.objects.get_or_create(username = request.user.username)
    
    personal_instance = get_object_or_404(Personal_detail, username = request.user.username)
    progress = progressreport.objects.get(username = request.user.username)
    
    if request.method == "POST":
        personalform = PersonalDetailsForm(request.POST, instance=personal_instance)

        if personalform.is_valid():
            new_entry = personalform.save(commit=False)
            new_entry.username = request.user.username
            new_entry.save()
            progress.personal_detail = True
            progress.save()
            messages.success(request, "Personal details added successfully!!")
            return redirect('/education')
    else:
        personalform = PersonalDetailsForm(instance=personal_instance)
    return render(request, 'personal_detail.html',{'personalform':personalform,'progress':progress})

# help user create account on the site and then render the same again to help him login to the site.
def signin(request):

    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if firstname != '' and lastname != '' and email != '':
            
            if password == confirmpassword:

                    username_flag = check_username(username)
                    email_flag = check_email(email)
                    
                    if username_flag == True:
                        messages.error(request, 'Username already in use.')
                        return redirect('/signin')
                    
                    elif email_flag == True:
                        messages.error(request, 'Email already registered.')
                    
                    elif username_flag == False and email_flag == False:
                        user = User.objects.create_user(first_name = firstname, last_name= lastname, username = username, email = email, password = password)
                        user.save()

                        messages.success(request, "Account created successfully!!")
                        return redirect('/signin')             
        
            else:
                messages.error(request, 'Both password and Confirm password fields have to be same.')
                return redirect('/signin')
        
        else:
            messages.error(request, "Please fill the complete form.")
            return redirect('/signin')
    
    return render(request, 'signin.html')

# def upload(request):
#     certificates.objects.get_or_create(username = request.user.username)
    
#     progress = progressreport.objects.get(username = request.user.username)
    
#     if request.method == "POST":
#         uploadform = CertificatesForm(request.POST, request.FILES)

#         if uploadform.is_valid():
#             new_entry = uploadform.save(commit=False)
#             new_entry.username = request.user.username
#             new_entry.save()
#             progress.certificates = True
#             progress.save()

#             messages.success(request, 'Certificates Uploaded')
#             messages.success(request, 'Phase 1 Completed Successfully!!')
#             return redirect('/upload')
#     else:
#         uploadform = CertificatesForm()
#     return render(request, 'upload.html',{'uploadform':uploadform,'progress':progress})
