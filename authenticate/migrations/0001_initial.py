# Generated by Django 5.0.2 on 2024-06-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accound_holder_name', models.CharField(max_length=70)),
                ('account_number', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Family_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(choices=[('Goverment Employee', 'Goverment Employee'), ('Private Sector', 'Private Sector'), ('Professional', 'Professional'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], max_length=20)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(choices=[('Goverment Employee', 'Goverment Employee'), ('Private Sector', 'Private Sector'), ('Professional', 'Professional'), ('Self-Employed', 'Self-Employed'), ('Home Maker', 'Home Maker')], max_length=20)),
                ('annual_income', models.CharField(choices=[('below 4 lakh', 'below 4 lakh'), ('between 4 to 8 lakh', 'between 4 to 8'), ('more than 8 lakhs', 'more than 8 lakhs')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(choices=[('pan card', 'Pan Card'), ('ration card', 'Ration Card'), ('passport', 'Passport'), ('adhar card', 'Adhar Card'), ('other', 'Other Valid Government Provided Id')], max_length=12)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=6)),
                ('mobile', models.CharField(max_length=13)),
                ('c_address', models.CharField(max_length=500)),
                ('p_address', models.CharField(max_length=500)),
                ('reservation', models.CharField(choices=[('unreserved', 'Unreserved'), ('sc', 'SC'), ('st', 'ST'), ('obc', 'OBC')], max_length=10)),
                ('special_reservation', models.CharField(choices=[('k-migrant', 'Kashmir Migrant'), ('staff quota', 'Staff Quota'), ('sports', 'Sports Quota'), ('pwd', 'PWD')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='school_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=500)),
                ('rollnumber', models.IntegerField()),
                ('result_status', models.CharField(choices=[('null', 'select'), ('pass', 'Passed'), ('appearing', 'Appearing')], max_length=10)),
                ('school_type', models.CharField(choices=[('null', 'select'), ('private', 'Private'), ('government', 'Government'), ('semi-government', 'Semi-government')], max_length=16)),
                ('school_name', models.CharField(max_length=250)),
                ('medium', models.CharField(choices=[('null', 'select'), ('hindi', 'Hindi'), ('english', 'English'), ('other', 'Other')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='subject_mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('political', 'Political Science')], max_length=10)),
                ('maximum1', models.CharField(max_length=4)),
                ('obtained1', models.CharField(max_length=4)),
                ('subject_percent1', models.CharField(max_length=4)),
                ('subject2', models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('political', 'Political Science')], max_length=10)),
                ('maximum2', models.CharField(max_length=4)),
                ('obtained2', models.CharField(max_length=4)),
                ('subject_percent2', models.CharField(max_length=4)),
                ('subject3', models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('political', 'Political Science')], max_length=10)),
                ('maximum3', models.CharField(max_length=4)),
                ('obtained3', models.CharField(max_length=4)),
                ('subject_percent3', models.CharField(max_length=4)),
                ('subject4', models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('political', 'Political Science')], max_length=10)),
                ('maximum4', models.CharField(max_length=4)),
                ('obtained4', models.CharField(max_length=4)),
                ('subject_percent4', models.CharField(max_length=4)),
                ('subject5', models.CharField(choices=[('maths', 'Mathematics'), ('english', 'English'), ('comp', 'Computer Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('bio', 'Biology'), ('accounts', 'Accounts'), ('economics', 'Economics'), ('business', 'Business Studies'), ('physical', 'Physical Sciences'), ('history', 'History'), ('geography', 'Geography'), ('political', 'Political Science')], max_length=10)),
                ('maximum5', models.CharField(max_length=4)),
                ('obtained5', models.CharField(max_length=4)),
                ('subject_percent5', models.CharField(max_length=4)),
            ],
        ),
    ]
