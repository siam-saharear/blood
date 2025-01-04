# from django import forms

# class Add_organ(forms.Form):
#         organ_system = forms.ChoiceField(choices=[])
#         organ_name = forms.CharField(max_length=40)
#         organ_function = forms.CharField(max_length=1200)
        
# class Search_organ(forms.Form):
#     organ_system = forms.ChoiceField(choices=[], required=False)
#     organ_name = forms.CharField(max_length=100, required=False)    


from django import forms
from .models import User, UseContactEmail, UseContactNumber

class  UserSignupForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=255, required=True)
    mname = forms.CharField(label="Middle Name", max_length=255, required=False)
    lname = forms.CharField(label="Last Name", max_length=255, required=True)
    utype = forms.ChoiceField(label="User Type", choices=[('aggriculturalofficer', 'Aggriculturalofficer'),
                                                          ('farmer', 'Farmer'),
                                                          ('wirehouse manaher', 'Wirehouse Manaher'),
                                                          ('distributor company', 'Distributor Company'),
                                                          ('admin', 'Admin'),
                                                           ('neutritionist', 'Neutritionist')])
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    email_addresses = forms.EmailField(label="Email Address", required=True)
    contact_number = forms.CharField(label="Contact Number", max_length=255, required=True)




class UserLoginForm(forms.Form):
    uid = forms.CharField(label="User ID", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)