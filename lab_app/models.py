from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PeopleCategory(models.Model):
    category = models.CharField(max_length=200,null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    

class PeopleProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='peopleprofile')
    category = models.ForeignKey(PeopleCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    affiliation = models.CharField(max_length=200, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profileImages')
    biography = models.TextField(null=True, blank=True)
    google_scholar = models.CharField(max_length=300, blank=True, null=True)
    research_gate = models.CharField(max_length=300, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Profile"
    

class Publication(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    doi_link = models.CharField(max_length=300,null=True,blank=True)
    publish_year = models.CharField(max_length=200,null=True,blank=True)
    publication_image = models.ImageField(upload_to='publication/images/',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        title_str = str(self.title) if self.title else "Untitled Publication"
        print(f"DEBUG: {title_str}")
        return title_str


class Education(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    degree = models.CharField(max_length=200,null=True)
    duration = models.CharField(max_length=200,null=True)
    university_or_school = models.CharField(max_length=200,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.degree
    

class Project(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    project_title = models.TextField(blank=True,null=True)
    project_description = models.TextField(blank=True,null=True)
    stat_date = models.CharField(max_length=200,null=True,blank=True)
    end_date = models.CharField(max_length=200,null=True,blank=True)
    department =models.CharField(max_length=200,null=True)
    funding_authority = models.CharField(max_length=200,null=True,blank=True)
    project_image = models.ImageField(upload_to='project/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}"
    


class Contact(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    office_address = models.TextField(blank=True,null=True)
    department = models.CharField(max_length=200,blank=True,null=True)
    faculty = models.CharField(max_length=200,blank=True,null=True)
    university = models.CharField(max_length=200,blank=True,null=True)
    post = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=14,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    skype = models.CharField(max_length=200,blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}"
    


class ResearchInterest(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    interest_name = models.CharField(max_length=300,null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)



class Research(models.Model):
    author = models.ForeignKey(PeopleProfile,on_delete=models.CASCADE)
    title = models.TextField(null=True,blank=True)
    project_image = models.ImageField(upload_to='research/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}"
    



class CentralContact(models.Model):
    office_address = models.TextField(blank=True,null=True)
    department = models.CharField(max_length=200,blank=True,null=True)
    faculty = models.CharField(max_length=200,blank=True,null=True)
    university = models.CharField(max_length=200,blank=True,null=True)
    post = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=14,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    skype = models.CharField(max_length=200,blank=True,null=True)
    address_image = models.ImageField('address/image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department}"



class About(models.Model):
    about_image = models.ImageField('about/image/',blank=True,null=True)
    about1 = models.TextField(blank=True,null=True)
    about2 = models.TextField(blank=True,null=True)
    about3 = models.TextField(blank=True,null=True)
    about4 = models.TextField(blank=True,null=True)
    about5 = models.TextField(blank=True,null=True)
    about6 = models.TextField(blank=True,null=True)
    about7 = models.TextField(blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.about1}"
    



class ContactUs(models.Model):
    full_name = models.CharField(max_length=200,null=False,blank=True)
    email = models.CharField(max_length=200,null=False,blank=False)
    phone = models.CharField(max_length=200,null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    submit_date = models.DateField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='imageGallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image.name)

