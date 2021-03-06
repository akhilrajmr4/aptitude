# Generated by Django 4.0.3 on 2022-03-22 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminlimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_question', models.IntegerField()),
                ('time_taken', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('qualifications', models.CharField(blank=True, max_length=100, null=True)),
                ('passout_year', models.IntegerField(blank=True, default='', null=True)),
                ('exam_status', models.CharField(default='0', max_length=20)),
                ('mark', models.IntegerField(default='0')),
                ('regdate', models.DateField(default='')),
                ('contact_status', models.CharField(default='0', max_length=20)),
                ('replay_status', models.CharField(default='0', max_length=20)),
                ('te_status', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no_of_question', models.CharField(max_length=100)),
                ('time_taken', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=100)),
                ('ctgry_id', models.CharField(default='', max_length=100)),
                ('dept_id', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='time_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_status', models.CharField(default='0', max_length=100)),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='app.catagory')),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='app.candidates')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('contact_no', models.CharField(default='', max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='images/')),
                ('designation', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='desgn', to='app.designation')),
            ],
        ),
        migrations.AddField(
            model_name='candidates',
            name='deptmnt',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dep', to='app.department'),
        ),
    ]
