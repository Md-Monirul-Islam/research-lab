from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'lab_app'

urlpatterns = [
    path('',views.home_page_view,name='home_page_view'),
    path('banner-image-upload/', views.upload_banner_image, name='banner_image_upload'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('profile/', views.view_profile, name='view_profile'),

    path('add-publication/', views.add_publication, name='add_publication'),
    path('my-publications/', views.view_publications, name='view_publications'),
    path('update-publication/<int:pk>/', views.update_publication, name='update_publication'),
    path('delete-publication/<int:pk>/', views.delete_publication, name='delete_publication'),

    path('add-education/', views.add_education, name='add_education'),
    path('view-education/', views.view_education, name='view_education'),
    path('update-education/<int:pk>/', views.update_education, name='update_education'),
    path('delete-education/<int:pk>/', views.delete_education, name='delete_education'),

    path('add-project/', views.add_project, name='add_project'),
    path('projects/', views.project_list, name='project_list'),
    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),

    path('add-contact/', views.add_contact, name='add_contact'),
    path('view-contacts/', views.view_contacts, name='view_contacts'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', views.delete_contact, name='delete_contact'),

    path('add-research-interest/', views.add_research_interest, name='add_research_interest'),
    path('research-interests/', views.view_research_interests, name='view_research_interests'),
    path('edit-research-interest/<int:pk>/', views.edit_research_interest, name='edit_research_interest'),
    path('delete-research-interest/<int:pk>/', views.delete_research_interest, name='delete_research_interest'),

    path('add-research/', views.add_research, name='add_research'),
    path('view-research/', views.view_research, name='view_research'),
    path('edit-research/<int:pk>/', views.edit_research, name='edit_research'),
    path('delete-research/<int:pk>/', views.delete_research, name='delete_research'),

    path('add-central-contact/', views.add_central_contact, name='add_central_contact'),
    path('central-contact-show/', views.view_central_contacts, name='view_central_contacts'),
    path('edit-central-contact/<int:pk>/', views.edit_central_contact, name='edit_central_contact'),
    path('delete-central-contact/<int:pk>/', views.delete_central_contact, name='delete_central_contact'),

    path('add-about/', views.add_about, name='add_about'),
    path('view-about/', views.view_about, name='view_about'),
    path('edit-about/<int:pk>/', views.edit_about, name='edit_about'),
    path('delete-about/<int:pk>/', views.delete_about, name='delete_about'),

    path('superuser-dashboard/',views.dashboard,name='bashboard'),

    path('add_category/', views.add_category, name='add_category'),
    path('all-categories-people-list/', views.people_list, name='all_people_list'),
    path('category/<str:category_name>/', views.category_people_list, name='category_people_list'),
    path('profiles/<int:pk>/', views.PeopleProfileDetailView.as_view(), name='people_profile_detail'),
    path('author/<int:author_id>/projects/', views.author_projects, name='author_projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('publications/', views.publication_list, name='publication_list'),
    path('author/<int:author_id>/publication/', views.author_publications, name='author_publications'),
    path('author/<int:author_id>/contact/', views.contact_info, name='contact_info'),
    path('author/<int:author_id>/research-interests/', views.research_interest_view, name='research_interest'),
    path('education/<int:author_id>/', views.author_education, name='author_education'),
    path('author/<int:author_id>/research/', views.author_research, name='author_researches'),
    path('research/<int:research_id>/', views.research_detail, name='research_detail'),
    path('central-contact/', views.public_central_contact, name='central_contact'),
    path('about/', views.about_view, name='about'),

    path('change-password/', views.change_password, name='change_password'),
    path('password-change-done/', views.password_change_done, name='password_change_done'),

    path('contact-us/', views.add_contact_us, name='add_contact_us'),
    path('contact-us-details/', views.contact_us_details_view, name='contact_us_details'),

    path('upload-images/', views.upload_images, name='upload_images'),
    # path('gallery/', views.image_gallery_view, name='image_gallery'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)