# Generated by Django 3.0.4 on 2020-03-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0011_auto_20200325_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_model',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign.team_model', to_field='name'),
        ),
        migrations.AlterField(
            model_name='leaders_model',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign.employee_model', to_field='name'),
        ),
    ]
