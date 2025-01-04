# from django.shortcuts import render, redirect
# from organs.models import Organ_systems, Organs
# from .forms import Add_organ, Search_organ

# # Create your views here.
# def organ_home(response):
#     organ_systems = []
#     return render(response, "organs/home.html", {"title":"Fresh Vault","organ_systems":organ_systems})




# def add_organ(response):
#     form = Add_organ(response.POST or None)
#     # print(f"\033[1;32;40m    \n\033[0m")
#     all_organ_systems = []
#     for i in range(len(Organ_systems.objects.all())):
#         all_organ_systems.append(Organ_systems.objects.get(id = i+1).organ_system)
    
#     form.fields["organ_system"].choices = [(organ, organ.capitalize()) for organ in all_organ_systems]
    
#     if response.method == "POST":        
#         if form.is_valid():
#             form_organ_system = form.cleaned_data["organ_system"]
#             form_organ_name = form.cleaned_data["organ_name"]
#             form_organ_function = form.cleaned_data["organ_function"]
#             # print(organ_system, organ_name , organ_function)
#             print(f"\033[1;32;40m FORM_DATA  \n{form_organ_system} {form_organ_name}  {form_organ_function}\n\033[0m")
            
            
#             all_organs = Organ_systems.objects.get(organ_system = form_organ_system).organs_set.all()
#             duplicate_found = False
#             for organ in all_organs:
#                 if organ.organ_name == form_organ_name:
#                     duplicate_found = True
#                     print(f"\033[1;32;40m  \nduplicate_found  \n\033[0m")
#             if duplicate_found != True:
#                     new = Organ_systems.objects.get(organ_system = form_organ_system).organs_set.create(organ_name = form_organ_name, organ_function= form_organ_function)
#                     new.save()
#                     print(new)
            
#         else:
            
#             print("hola")
#         # print(form)            
#     return render(response, "organs/add_organ.html", {"title":"Add organ", "form":form,  "all_organ_systems":all_organ_systems})





# def search_organ(response):
#     form = Search_organ(response.POST or None)
#     all_organ_systems = [""]
#     message = ""
    
#     for organ_system in (Organ_systems.objects.all()):
#         all_organ_systems.append(organ_system.organ_system)
    
#     form.fields["organ_system"].choices = [(organ, organ.capitalize()) for organ in all_organ_systems]

#     if response.method == "POST":
#         if form.is_valid():
#             form_organ_system = form.cleaned_data["organ_system"]
#             form_organ_name = form.cleaned_data["organ_name"]
#             # print(form_organ_system)
#             print(f"\033[1;32;40m  {form_organ_name} {form_organ_system}  \n\033[0m")
#             print(f":{type(form_organ_name)}:")
#             if form_organ_system!="":
#                 if form_organ_name!="":
#                     # "NONE OF THEM ARE EMPTY"
#                     # redirect to organ_system/organ_name
#                     found_organ = None
#                     try:
#                         found_organ = Organs.objects.get(organ_name = form_organ_name)
#                     except:
#                         message = "Invalid Organ_name" 
#                     if found_organ != None:
#                         return redirect(f"http://127.0.0.1:8000/{form_organ_system}/{form_organ_name}")
                                

#                 else:
#                     # SYSTEM IS NOT EMPTY BUT ORGAN IS
#                     print("redirect to organ_system_individual page")
#                     return redirect(f"http://127.0.0.1:8000/{form_organ_system}")
#             else:
#                 if form_organ_name!="":
#                     # SYSTEM IS EMPTY BUT ORGAN IS NOT
#                     print("redirect to one organ only page")
#                     found_organ = None
#                     try:
#                         found_organ = Organs.objects.get(organ_name = form_organ_name)
#                     except:
#                         message = "Invalid Organ_name" 
#                     if found_organ != None:
#                         organ_system = Organs.objects.get(organ_name = form_organ_name).organ_system
#                         message = f"{form_organ_name} is a part of {organ_system}_system"
#                         return redirect(f"http://127.0.0.1:8000/{organ_system}/{form_organ_name}")
#                 else:
#                     # BOTH OF THEM ARE EMPTY
#                     message = "Enter organ_system or organ_name dumbass"
#                     print("return to search page")

#         else:
#             print(form)
#             print("form not valid")
#     return render(response, "organs/search_organ.html", {"title":"search_organ", "form" : form, "all_organ_systems" : all_organ_systems, "message":message})


# # dont take out request, or it wont work
# def individual_organ_system(request, organ_system):
#     #                     # WITH DICT
#     # organs = {}
    
#     # for i in range(len(Organ_systems.objects.get(organ_system = organ_system).organs_set.all())):
#     #     try:            
#     #         organs_query = Organ_systems.objects.get(organ_system=organ_system).organs_set.all()            
#     #         for organ in organs_query:
#     #             organs[organ.organ_name] = organ.organ_function            
#     #     except:
#     #         pass
#     organs = []
#     organs_query = Organ_systems.objects.get(organ_system = organ_system).organs_set.all()
#     print(organs_query)
#     for organ in organs_query:
#         organs.append(organ.organ_name) 
    
#     return render(request, "organs/individual_organ_system.html", {"title":organ_system.title(),"organs": organs, "organ_system":organ_system})


# def individual_organ(request, organ_system, organ):
#     try:
#         found_organ = Organ_systems.objects.get(organ_system=organ_system).organs_set.get(organ_name = organ)
#     except:
#         pass
#     if found_organ :
#         organ_name = found_organ.organ_name
#         organ_function = found_organ.organ_function
#         return render(request, "organs/individual_organ.html", {"title":found_organ, "organ_name":organ_name, "organ_function":organ_function})
#     return render(request, "organs/individual_organ.html", {"title":"bal"})
    
    
    
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserSignupForm
from .models import User, UseContactEmail, UseContactNumber
def signup(request):
    # Get the total number of rows in the User table
    user_count = User.objects.count()

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            fname = form.cleaned_data['fname']
            mname = form.cleaned_data['mname']
            lname = form.cleaned_data['lname']
            utype = form.cleaned_data['utype']
            password = form.cleaned_data['password']
            email_addresses = form.cleaned_data['email_addresses']
            contact_number = form.cleaned_data['contact_number']

            # Save user data to the database
            user = User(
                fname=fname,
                mname=mname,
                lname=lname,
                utype=utype,
                password=make_password(password)  # Hash the password
            )
            user.save()

            # Save contact email and number
            UseContactEmail.objects.create(uid=user, email_addresses=email_addresses)
            UseContactNumber.objects.create(uid=user, contact_number=contact_number)

            # Redirect to the same page after successful sign-up
            return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form, 'user_count': user_count+1})








from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User
from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['uid']
            password = form.cleaned_data['password']

            # Authenticate user
            try:
                user = User.objects.get(uid=uid)
                if check_password(password, user.password):
                    # Set session
                    request.session['uid'] = user.uid
                    request.session['fname'] = user.fname
                    messages.success(request, "Logged in successfully!")
                    return redirect('home')  # Redirect to a home page or dashboard
                else:
                    messages.error(request, "Invalid password!")
            except User.DoesNotExist:
                messages.error(request, "User ID does not exist!")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



def logout(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # Redirect to login page


def home(request):
    if 'uid' not in request.session:
        return redirect('login')  # Redirect to login if not authenticated
    return render(request, 'home.html', {'fname': request.session.get('fname')})
