from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import About, BannerImage, CentralContact, Contact, ContactUs, Education, ImageGallery, PeopleCategory, PeopleProfile, Project, Publication, Research, ResearchInterest


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']

    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class PeopleCategoryForm(forms.ModelForm):
    class Meta:
        model = PeopleCategory
        fields = ['category']


class PeopleProfileForm(forms.ModelForm):
    class Meta:
        model = PeopleProfile
        fields = ['category', 'name', 'position', 'department', 'affiliation', 'profile_photo', 'biography', 'google_scholar', 'research_gate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your position'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your department'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your affiliation'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your biography'}),
            'google_scholar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Google Scholar Profile URL'}),
            'research_gate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Research Gate Profile URL'}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'doi_link', 'publish_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'doi_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter DOI Link'}),
            'publish_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Publish Year'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'duration', 'university_or_school']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter degree'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration'}),
            'university_or_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter university or school'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_description', 'stat_date', 'end_date', 'department', 'funding_authority', 'project_image']
        widgets = {
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter project description'}), #'rows': 4
            'stat_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter project title'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter department'}),
            'funding_authority': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter funding authority'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'office_address', 'department', 'faculty', 'university', 
            'post', 'phone', 'email', 'skype'
        ]
        widgets = {
            'office_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ResearchInterestForm(forms.ModelForm):
    class Meta:
        model = ResearchInterest
        fields = ['interest_name']
        widgets = {
            'interest_name': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your research interest'
            }),
        }



class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['title', 'project_image']
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your research title'
            }),
        }



class CentralContactForm(forms.ModelForm):
    class Meta:
        model = CentralContact
        fields = [
            'office_address', 'department', 'faculty', 'university', 
            'post', 'phone', 'email', 'skype', 'address_image'
        ]
        widgets = {
            'office_address': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter office address'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter department'
            }),
            'faculty': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter faculty'
            }),
            'university': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter university'
            }),
            'post': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter post'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter email'
            }),
            'skype': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Skype ID'
            }),
            'address_image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }



class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['about_image', 'about1', 'about2', 'about3', 'about4', 'about5', 'about6', 'about7']
        widgets = {
            'about_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'about1': forms.Textarea(attrs={'class': 'form-control', }),
            'about2': forms.Textarea(attrs={'class': 'form-control', }),
            'about3': forms.Textarea(attrs={'class': 'form-control', }),
            'about4': forms.Textarea(attrs={'class': 'form-control', }),
            'about5': forms.Textarea(attrs={'class': 'form-control', }),
            'about6': forms.Textarea(attrs={'class': 'form-control', }),
            'about7': forms.Textarea(attrs={'class': 'form-control', }), #'rows': 3
        }



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'type':'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'type':'number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                # 'rows': 5,
            }),
        }



class ImageGalleryForm(forms.ModelForm):
    
    class Meta:
        model = ImageGallery
        fields = ['image',]
