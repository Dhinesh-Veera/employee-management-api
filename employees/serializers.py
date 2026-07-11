from .models import Employee, Department
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Employee must be at least 18 years old.")

        if value > 60:
            raise serializers.ValidationError("Employee age cannot exceed 60")

        return value

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than 0")

        return value

    def validate(self, attrs):

        role = attrs.get("role")
        salary = attrs.get("salary")

        if role.lower() == "manager" and salary < 50000:
            raise serializers.ValidationError({"salary": "Manager salary must br at least 50000"})

        return attrs
