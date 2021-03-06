# Generated by Django 3.2.12 on 2022-03-24 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='deptmnt',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep', to='app.department'),
        ),
        migrations.AlterField(
            model_name='login',
            name='designation',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desgn', to='app.designation'),
        ),
        migrations.AlterField(
            model_name='time_out',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='app.catagory'),
        ),
        migrations.AlterField(
            model_name='time_out',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='app.candidates'),
        ),
    ]
