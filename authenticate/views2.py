from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

class FamilyDetailViewSet(viewsets.ModelViewSet):
    queryset = Family_detail.objects.all()
    serializer_class = FamilyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = Personal_detail.objects.all()
    serializer_class = PersonalDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class SchoolDetailViewSet(viewsets.ModelViewSet):
    queryset = school_detail.objects.all()
    serializer_class = SchoolDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubjectMarksViewSet(viewsets.ModelViewSet):
    queryset = subject_mark.objects.all()
    serializer_class = SubjectMarkSerializer
    permission_classes = [permissions.IsAuthenticated]

class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = bank_detail.objects.all()
    serializer_class = BankDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
