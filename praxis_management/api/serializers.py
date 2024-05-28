from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name',
                  'email','username','password','avatar']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id","first_name","last_name","phone_number","photo","specialization"
        ]

class NurseSerializer(ModelSerializer):
    class Meta:
        model = Nurse
        fields = [
            "id","first_name","last_name","phone_number","specialization"
        ]

class PatientSerializer(ModelSerializer):
    doctors = DoctorSerializer(many=True)
    nurses = NurseSerializer(many=True)
    class Meta:
        model = Patient
        fields = [
            "id","first_name","last_name",
            "phone_number","paid","actual_pay","doctors",
            "nurses","next_appointment","x_ray"
        ]