# Generated by Django 3.1 on 2020-08-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]