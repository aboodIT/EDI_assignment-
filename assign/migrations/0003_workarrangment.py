# Generated by Django 3.0.4 on 2020-03-20 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0002_employee_model_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workarrangment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_time', models.BooleanField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign.Employee_model')),
            ],
        ),
    ]
