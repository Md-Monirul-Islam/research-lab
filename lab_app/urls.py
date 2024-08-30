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
    path('central-contact/', views.central_contact_view, name='central_contact'),
    path('about/', views.about_view, name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)