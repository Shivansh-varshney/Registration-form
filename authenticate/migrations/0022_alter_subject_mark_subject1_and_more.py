# Generated by Django 5.0.2 on 2024-06-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0021_alter_personal_detail_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_mark',
            name='subject1',
            field=models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('hindi', 'Hindi'), ('sanskrit', 'Sanskrit'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('psycology', 'Psycology'), ('political', 'Political Science')], max_length=10),
        ),
        migrations.AlterField(
            model_name='subject_mark',
            name='subject2',
            field=models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('hindi', 'Hindi'), ('sanskrit', 'Sanskrit'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('psycology', 'Psycology'), ('political', 'Political Science')], max_length=10),
        ),
        migrations.AlterField(
            model_name='subject_mark',
            name='subject3',
            field=models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('hindi', 'Hindi'), ('sanskrit', 'Sanskrit'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('psycology', 'Psycology'), ('political', 'Political Science')], max_length=10),
        ),
        migrations.AlterField(
            model_name='subject_mark',
            name='subject4',
            field=models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('hindi', 'Hindi'), ('sanskrit', 'Sanskrit'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('psycology', 'Psycology'), ('political', 'Political Science')], max_length=10),
        ),
        migrations.AlterField(
            model_name='subject_mark',
            name='subject5',
            field=models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('hindi', 'Hindi'), ('sanskrit', 'Sanskrit'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('psycology', 'Psycology'), ('political', 'Political Science')], max_length=10),
        ),
    ]
