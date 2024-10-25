from rest_framework import serializers
from .models import *

class FamilyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family_detail
        fields = '__all__'

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_detail
        fields = '__all__'

class SchoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = school_detail
        fields = '__all__'

class SubjectMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject_mark
        fields = '__all__'

class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank_detail
        fields = '__all__'

