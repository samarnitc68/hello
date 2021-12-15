# Generated by Django 3.2.10 on 2021-12-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]