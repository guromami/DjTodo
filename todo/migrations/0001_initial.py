# Generated by Django 3.2.12 on 2022-02-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=5, verbose_name='NAME')),
                ('todo', models.CharField(max_length=50, verbose_name='TODO')),
            ],
        ),
    ]
