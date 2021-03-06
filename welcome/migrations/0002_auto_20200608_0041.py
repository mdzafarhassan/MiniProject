# Generated by Django 2.2.5 on 2020-06-07 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(max_length=10, unique=True)),
                ('cat_desc', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField()),
                ('created_by', models.CharField(max_length=10)),
                ('last_modified_date', models.DateTimeField()),
                ('last_modified_by', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'blog_category',
            },
        ),
        migrations.AddField(
            model_name='bookmaster',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('privacy_level', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='welcome.BlogCategory')),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog_post',
            },
        ),
    ]
