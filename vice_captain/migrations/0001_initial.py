# Generated by Django 3.0.2 on 2020-02-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vice_Captain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('votes', models.IntegerField()),
                ('vice_captain_slug', models.SlugField(blank=True)),
            ],
        ),
    ]
