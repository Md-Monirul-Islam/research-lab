# Generated by Django 4.2.15 on 2025-01-08 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='about/image/')),
                ('about1', models.TextField(blank=True, null=True)),
                ('about2', models.TextField(blank=True, null=True)),
                ('about3', models.TextField(blank=True, null=True)),
                ('about4', models.TextField(blank=True, null=True)),
                ('about5', models.TextField(blank=True, null=True)),
                ('about6', models.TextField(blank=True, null=True)),
                ('about7', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CentralContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_address', models.TextField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('faculty', models.CharField(blank=True, max_length=200, null=True)),
                ('university', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('skype', models.CharField(blank=True, max_length=200, null=True)),
                ('address_image', models.ImageField(upload_to='', verbose_name='address/image/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('submit_date', models.DateField(auto_now_add=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imageGallery/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('affiliation', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.ImageField(upload_to='profileImages')),
                ('biography', models.TextField(blank=True, null=True)),
                ('google_scholar', models.CharField(blank=True, max_length=300, null=True)),
                ('research_gate', models.CharField(blank=True, max_length=300, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peoplecategory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='peopleprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(blank=True, max_length=300, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('project_image', models.ImageField(upload_to='research/images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('doi_link', models.CharField(blank=True, max_length=300, null=True)),
                ('publish_year', models.CharField(blank=True, max_length=200, null=True)),
                ('publication_image', models.ImageField(blank=True, null=True, upload_to='publication/images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.TextField(blank=True, null=True)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('stat_date', models.CharField(blank=True, max_length=200, null=True)),
                ('end_date', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('funding_authority', models.CharField(blank=True, max_length=200, null=True)),
                ('project_image', models.ImageField(upload_to='project/images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200, null=True)),
                ('duration', models.CharField(max_length=200, null=True)),
                ('university_or_school', models.CharField(max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_address', models.TextField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('faculty', models.CharField(blank=True, max_length=200, null=True)),
                ('university', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('skype', models.CharField(blank=True, max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_app.peopleprofile')),
            ],
        ),
    ]
