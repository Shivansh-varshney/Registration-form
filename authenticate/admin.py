from django.contrib import admin
from .models import *

# register your model using decorators


@admin.register(Family_detail)
class Family_detailAdmin(admin.ModelAdmin):
    list_display = ('username', 'father_name', 'father_occupation',
                    'mother_name', 'mother_occupation', 'annual_income')


@admin.register(Personal_detail)
class Personal_detailAdmin(admin.ModelAdmin):
    list_display = ('username', 'identity', 'date_of_birth', 'gender', 'mobile',
                    'correspondance_address', 'permanent_address', 'reservation', 'special_reservation')


@admin.register(school_detail)
class school_detailAdmin(admin.ModelAdmin):
    list_display = ('username', 'board', 'rollnumber',
                    'result_status', 'school_type', 'school_name', 'medium')


@admin.register(bank_detail)
class bank_detailAdmin(admin.ModelAdmin):
    list_display = ('username', 'accound_holder_name',
                    'account_number', 'bank_name', 'ifsc')


@admin.register(subject_mark)
class subject_markAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject1', 'maximum_marks_Sub1', 'obtained_marks_Sub1', 'subject2', 'maximum_marks_Sub2', 'obtained_marks_Sub2',
                    'subject3', 'maximum_marks_Sub3', 'subject4', 'maximum_marks_Sub4', 'obtained_marks_Sub4', 'subject5', 'maximum_marks_Sub5', 'obtained_marks_Sub5')


@admin.register(progressreport)
class progressreportAdmin(admin.ModelAdmin):
    list_display = ('username', 'family_detail',
                    'personal_detail', 'education', 'bank_detail')


# Register your models here.
