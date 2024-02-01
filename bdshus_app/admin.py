from django.contrib import admin
from .models import *


class BankAdmin(admin.ModelAdmin):
    list_display = ("bank_number", "bank_name")


class CardAdmin(admin.ModelAdmin):
    list_display = ("pay_acc_numb", "number_card", "bank_number", "student_code")


class DivisionAdmin(admin.ModelAdmin):
    list_display = ("division_code", "division_name")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "last_name", "middle_name", "first_name", "division_code")


class FacultetAdmin(admin.ModelAdmin):
    list_display = ("facultet_code", "facultet_name")


class PurposeAdmin(admin.ModelAdmin):
    list_display = ("purpose_id", "purpose_sum", "purpose_date", "scholarship", "pay_acc_numb")


class ScholarshipPurposeAdmin(admin.ModelAdmin):
    list_display = ("scholarship_id", "purpose_date", "type", "student_code", "employee")


class ScholarshipTypeAdmin(admin.ModelAdmin):
    list_display = ("type_id", "type_name")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_code", "last_name", "first_name", "middle_name", "birth_date", "facultet_code")


admin.site.register(Bank, BankAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Facultet, FacultetAdmin)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(ScholarshipPurpose, ScholarshipPurposeAdmin)
admin.site.register(ScholarshipType, ScholarshipTypeAdmin)
admin.site.register(Student, StudentAdmin)
