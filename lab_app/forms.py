from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import BannerImage, Education, PeopleCategory, PeopleProfile, Publication


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