from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import DetailView
from django.http import Http404
from lab_app.forms import AboutForm, BannerImageForm, CentralContactForm, ContactForm, ContactUsForm, EducationForm, ImageGalleryForm,LoginForm, PeopleCategoryForm, PeopleProfileForm, ProjectForm, PublicationForm, ResearchForm, ResearchInterestForm, SignUpForm
from lab_app.models import About, BannerImage, CentralContact, Contact, ContactUs, Education, ImageGallery, PeopleCategory, PeopleProfile, Project, Publication, Research, ResearchInterest

# Create your views here.
def home_page_view(request):
    banner_images = BannerImage.objects.order_by('-uploaded_at')[:3]
    project = Project.objects.latest('id') if Project.objects.exists() else None
    research = Research.objects.latest('id') if Research.objects.exists() else None
    publication = Publication.objects.latest('id') if Publication.objects.exists() else None
    profile = PeopleProfile.objects.first()
    context = {
        'banner_images': banner_images,
        'project': project,
        'research': research,
        'publication': publication,
        'profile':profile,
    }
    return render(request, 'lab_app/home.html', context)




@login_required
@permission_required('lab_app.add_bannerimage')
def upload_banner_image(request):
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner image uploaded successfully!')
            return redirect('lab_app:home_page_view')
    else:
        form = BannerImageForm()
    return render(request, 'lab_app/banner_image_upload_form.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('lab_app:home_page_view')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'lab_app/login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successfully')
            return redirect('lab_app:home_page_view')
        else:
            messages.error(request, "Signup not successfully")
    else:
        form = SignUpForm()
    return render(request, 'lab_app/signup.html', {'form': form})



@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('lab_app:login')



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('lab_app:password_change_done')
        else:
            messages.error(request, 'Please correct submit correctly.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'lab_app/change_password.html', {'form': form})



def password_change_done(request):
    return render(request, 'lab_app/password_change_done.html')



@login_required
def update_profile(request):
    profile = request.user.peopleprofile
    if request.method == 'POST':
        form = PeopleProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')
            return redirect('lab_app:home_page_view')
        else:
            messages.error(request, "Profile not update successfully")
    else:
        form = PeopleProfileForm(instance=profile)
    
    return render(request, 'lab_app/update_profile.html', {'form': form})



@login_required
def view_profile(request):
    # Get the profile for the currently logged-in user
    profile = get_object_or_404(PeopleProfile, user=request.user)
    
    return render(request, 'lab_app/view_profile.html', {'profile': profile})



@login_required
def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.author = request.user.peopleprofile  # Assign the logged-in user's profile
            publication.save()
            messages.success(request, 'Publication added successfully')
            return redirect('lab_app:view_publications')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = PublicationForm()

    return render(request, 'lab_app/add_publication.html', {'form': form})



@login_required
def view_publications(request):
    publications = Publication.objects.filter(author=request.user.peopleprofile)
    return render(request, 'lab_app/view_publications.html', {'publications': publications})




@login_required
def update_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication update successfully')
            return redirect('lab_app:view_publications')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = PublicationForm(instance=publication)

    return render(request, 'lab_app/add_publication.html', {'form': form})




@login_required
def delete_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        publication.delete()
        messages.success(request, 'Publication delete successfully')
        return redirect('lab_app:view_publications')

    return render(request, 'lab_app/confirm_delete_publication.html', {'publication': publication})




@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.author = request.user.peopleprofile  # Assuming you have a related PeopleProfile
            education.save()
            messages.success(request, 'Education added successfully')
            return redirect('lab_app:view_education')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = EducationForm()
    return render(request, 'lab_app/add_education.html', {'form': form})



@login_required
def view_education(request):
    user_profile = request.user.peopleprofile  # Assuming you have a related PeopleProfile
    education_list = Education.objects.filter(author=user_profile)
    return render(request, 'lab_app/view_education.html', {'education_list': education_list})



@login_required
def update_education(request, pk):
    education = get_object_or_404(Education, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education update successfully')
            return redirect('lab_app:view_education')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = EducationForm(instance=education)

    return render(request, 'lab_app/add_education.html', {'form': form})




@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education delete successfully')
        return redirect('lab_app:view_education')

    return render(request, 'lab_app/confirm_delete.html', {'education': education})




@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user.peopleprofile
            project.save()
            messages.success(request, 'Project add successfully')
            return redirect('lab_app:project_list')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ProjectForm()
    return render(request, 'lab_app/add_project.html', {'form': form})



@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'lab_app/project_list.html', {'projects': projects})



@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project edit successfully')
            return redirect('lab_app:project_list')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ProjectForm(instance=project)

    return render(request, 'lab_app/edit_project.html', {'form': form, 'project': project})




@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project delete successfully')
        return redirect('lab_app:project_list')

    return render(request, 'lab_app/confirm_delete_project.html', {'project': project})





@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user.peopleprofile
            contact.save()
            messages.success(request, 'Contact add successfully')
            return redirect('lab_app:view_contacts')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ContactForm()
    return render(request, 'lab_app/add_contact.html', {'form': form})



@login_required
def view_contacts(request):
    contacts = Contact.objects.filter(author=request.user.peopleprofile)
    return render(request, 'lab_app/view_contacts.html', {'contacts': contacts})




@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact edit successfully')
            return redirect('lab_app:view_contacts')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ContactForm(instance=contact)

    return render(request, 'lab_app/edit_contact.html', {'form': form})



@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact delete successfully')
        return redirect('lab_app:view_contacts')

    return render(request, 'lab_app/confirm_delete_contact.html', {'contact': contact})





@login_required
def add_research_interest(request):
    if request.method == 'POST':
        form = ResearchInterestForm(request.POST)
        if form.is_valid():
            research_interest = form.save(commit=False)
            research_interest.author = request.user.peopleprofile
            research_interest.save()
            messages.success(request, 'Research Interest added successfully')
            return redirect('lab_app:view_research_interests')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ResearchInterestForm()

    return render(request, 'lab_app/add_research_interest.html', {
        'form': form,
        'form_type': 'add'
    })



@login_required
def view_research_interests(request):
    research_interests = ResearchInterest.objects.filter(author=request.user.peopleprofile)
    return render(request, 'lab_app/view_research_interests.html', {'research_interests': research_interests})



@login_required
def edit_research_interest(request, pk):
    research_interest = get_object_or_404(ResearchInterest, pk=pk, author=request.user.peopleprofile)

    if request.method == 'POST':
        form = ResearchInterestForm(request.POST, instance=research_interest)
        if form.is_valid():
            form.save()
            messages.success(request, 'Research Interest updated successfully')
            return redirect('lab_app:view_research_interests')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ResearchInterestForm(instance=research_interest)

    return render(request, 'lab_app/add_research_interest.html', {
        'form': form,
        'form_type': 'edit'
    })



@login_required
def delete_research_interest(request, pk):
    interest = get_object_or_404(ResearchInterest, pk=pk, author=request.user.peopleprofile)
    
    if request.method == 'POST':
        interest.delete()
        messages.success(request, 'Research Interest deleted successfully')
        return redirect('lab_app:view_research_interests')
    
    return render(request, 'lab_app/confirm_delete_research_interest.html', {'interest': interest})







@login_required
def add_research(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            research = form.save(commit=False)
            research.author = request.user.peopleprofile
            research.save()
            messages.success(request, 'Research added successfully')
            return redirect('lab_app:view_research')
        else:
            messages.error(request, "Somethings went wrong!!")
    else:
        form = ResearchForm()
    
    return render(request, 'lab_app/add_research.html', {
        'form': form,
        'form_type': 'edit'
    })




@login_required
def view_research(request):
    research_projects = Research.objects.filter(author=request.user.peopleprofile)
    return render(request, 'lab_app/view_research.html', {'research_projects': research_projects})



@login_required
def edit_research(request, pk):
    research = get_object_or_404(Research, pk=pk)

    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES, instance=research)
        if form.is_valid():
            form.save()
            messages.success(request, "Research project updated successfully!")
            return redirect('lab_app:view_research')
        else:
            messages.error(request, "Something went wrong. Please check the form and try again.")
    else:
        form = ResearchForm(instance=research)

    return render(request, 'lab_app/add_research.html', {
        'form': form,
        'form_type': 'edit'
    })



@login_required
def delete_research(request, pk):
    research = get_object_or_404(Research, pk=pk)

    if request.method == 'POST':
        research.delete()
        messages.success(request, "Research project deleted successfully!")
        return redirect('lab_app:view_research')

    return render(request, 'lab_app/delete_research.html', {'research': research})




@login_required
def add_central_contact(request):
    if request.method == 'POST':
        form = CentralContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Central Contact added successfully!")
            return redirect('lab_app:view_central_contacts')
        else:
            messages.error(request, "There was an error adding the Central Contact.")
    else:
        form = CentralContactForm()
    
    return render(request, 'lab_app/add_central_contact.html', {
        'form': form,
        'form_type': 'edit'
    })



def view_central_contacts(request):
    contacts = CentralContact.objects.all()
    return render(request, 'lab_app/view_central_contacts.html', {'contacts': contacts})



@login_required
def edit_central_contact(request, pk):
    contact = get_object_or_404(CentralContact, pk=pk)

    if request.method == 'POST':
        form = CentralContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Central Contact updated successfully!")
            return redirect('lab_app:view_central_contacts')
        else:
            messages.error(request, "There was an error adding the Central Contact.")
    else:
        form = CentralContactForm(instance=contact)
    
    return render(request, 'lab_app/add_central_contact.html', {
        'form': form,
        'form_type': 'edit'
    })



@login_required
def delete_central_contact(request, pk):
    contact = get_object_or_404(CentralContact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Central Contact deleted successfully!")
        return redirect('lab_app:view_central_contacts')

    return render(request, 'lab_app/confirm_delete_central_contact.html', {'contact': contact})




@login_required
def add_about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "About added successfully!")
            return redirect('lab_app:view_about')
        else:
            messages.error(request, "There was an error adding the Central Contact.")
    else:
        form = AboutForm()
    
    return render(request, 'lab_app/add_about.html', {'form': form})



def view_about(request):
    about_entries = About.objects.all()
    return render(request, 'lab_app/view_about.html', {'about_entries': about_entries})



@login_required
def edit_about(request, pk):
    about = get_object_or_404(About, pk=pk)
    
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('lab_app:view_about')
    else:
        form = AboutForm(instance=about)
    
    context = {
        'form': form,
        'form_type': 'edit'
    }
    return render(request, 'lab_app/add_about.html', context)



@login_required
def delete_about(request, pk):
    about = get_object_or_404(About, pk=pk)

    if request.method == 'POST':
        about.delete()
        return redirect('lab_app:view_about')

    return render(request, 'lab_app/confirm_delete_about.html', {'about': about})




def dashboard(request):
    return render(request,'lab_app/dashboard.html')



@login_required
@permission_required('lab_app.add_peoplecategory')
def add_category(request):
    if request.method == 'POST':
        form = PeopleCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category added successfully!')
            return redirect('lab_app:home_page_view')
    else:
        form = PeopleCategoryForm()
    return render(request, 'lab_app/add_category.html', {'form': form})




def people_list(request):
    categories = PeopleCategory.objects.all()
    profiles = PeopleProfile.objects.exclude(category__category="Default Category")
    return render(request, 'lab_app/people_list.html', {'categories': categories, 'profiles': profiles})


def category_people_list(request, category_name):
    try:
        category = PeopleCategory.objects.get(category=category_name)
        profiles = PeopleProfile.objects.filter(category=category)
        return render(request, 'lab_app/category_people_list.html', {'category': category, 'profiles': profiles})
    except PeopleCategory.DoesNotExist:
        return render(request, 'lab_app/category_people_list.html', {'category': None, 'profiles': []})



class PeopleProfileDetailView(DetailView):
    model = PeopleProfile
    template_name = 'lab_app/people_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['research_interests'] = ResearchInterest.objects.filter(author=self.object)
        context['related_projects'] = Project.objects.filter(author=self.object)[:5]
        return context




def author_projects(request, author_id):
    try:
        author = PeopleProfile.objects.get(id=author_id)
    except PeopleProfile.DoesNotExist:
        raise Http404("Author does not exist")
    
    projects = Project.objects.filter(author=author)
    
    if not projects.exists():
        messages.warning(request, "This author has no associated projects.")

    return render(request, 'lab_app/author_projects.html', {'author': author, 'projects': projects})



def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.filter(author=project.author).exclude(id=project.id)
    return render(request, 'lab_app/project_detail.html', {'project': project, 'related_projects': related_projects})



def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'lab_app/publication_list.html', {'publications': publications})




def author_publications(request, author_id):
    author = get_object_or_404(PeopleProfile, id=author_id)
    publications = Publication.objects.filter(author=author)
    return render(request, 'lab_app/author_publications.html', {'author': author, 'publications': publications})



def contact_info(request, author_id):
    author = get_object_or_404(PeopleProfile, id=author_id)
    try:
        contact = Contact.objects.get(author=author)
    except Contact.DoesNotExist:
        contact = None  # Set contact to None if it doesn't exist

    return render(request, 'lab_app/contact_info.html', {'author': author, 'contact': contact})


def research_interest_view(request, author_id):
    author = get_object_or_404(PeopleProfile, pk=author_id)
    research_interests = ResearchInterest.objects.filter(author=author)
    return render(request, 'lab_app/research_interest.html', {
        'author': author,
        'research_interests': research_interests,
    })



def author_education(request, author_id):
    author = get_object_or_404(PeopleProfile, id=author_id)
    education_records = Education.objects.filter(author=author)
    return render(request, 'lab_app/author_education.html', {
        'education_records': education_records,
        'author': author,
    })



def author_research(request, author_id):
    try:
        author = PeopleProfile.objects.get(id=author_id)
    except PeopleProfile.DoesNotExist:
        raise Http404("Author does not exist")
    
    research = Research.objects.filter(author=author)
    
    if not research.exists():
        messages.warning(request, "This author has no associated projects.")

    return render(request, 'lab_app/author_research.html', {'author': author, 'research': research})



def research_detail(request, research_id):
    try:
        research = Research.objects.get(id=research_id)
    except Research.DoesNotExist:
        return render(request, '404.html', status=404)
    related_research = Research.objects.filter(author=research.author).exclude(id=research.id)
    return render(request, 'lab_app/research_detail.html', {
        'research': research,
        'related_research': related_research
    })



# def public_central_contact(request):
#     contacts = CentralContact.objects.all()
#     return render(request, 'lab_app/publict_central_contact.html', {'contacts': contacts})
def public_central_contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_app:home_page_view')
    else:
        form = ContactUsForm()

    contacts = CentralContact.objects.all()
    return render(request, 'lab_app/public_central_contact.html', {
        'contacts': contacts,
        'form': form
    })



def about_view(request):
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'lab_app/about.html', context)




def add_contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Submit your contact successfully!")
            return redirect('lab_app:home_page_view')
        else:
            messages.error(request, "There was an error adding Contact.")
    else:
        form = ContactUsForm()
    return render(request, 'lab_app/add_contact_us.html', {'form': form})



@login_required
def contact_us_details_view(request):
    contact_us_entries = ContactUs.objects.all().order_by('-id')
    return render(request, 'lab_app/contact_us_details.html', {'contact_us_entries': contact_us_entries})




@login_required
def upload_images(request):
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle multiple files
            images = request.FILES.getlist('image')
            for image in images:
                ImageGallery.objects.create(image=image)
            messages.success(request, "Images uploaded successfully!")
            return redirect('lab_app:image_gallery')
        else:
            messages.error(request, "Somethsings went wrong!")
    else:
        form = ImageGalleryForm()
    
    context = {'form': form}
    return render(request, 'lab_app/upload_images.html', context)




def image_gallery_view(request):
    images = ImageGallery.objects.all().order_by('-id')
    context = {
        'images': images,
    }
    return render(request, 'lab_app/image_gallery.html', context)