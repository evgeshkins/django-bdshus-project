# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bank(models.Model):
    bank_number = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bank'


class Card(models.Model):
    pay_acc_numb = models.AutoField(primary_key=True)
    number_card = models.CharField(max_length=16)
    bank_number = models.ForeignKey(Bank, models.DO_NOTHING, db_column='bank_number', blank=True, null=True)
    student_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'


class Division(models.Model):
    division_code = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'division'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    division_code = models.ForeignKey(Division, models.DO_NOTHING, db_column='division_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Facultet(models.Model):
    facultet_code = models.AutoField(primary_key=True)
    facultet_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facultet'


class Purpose(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    purpose_sum = models.FloatField()
    purpose_date = models.DateField()
    scholarship = models.ForeignKey('ScholarshipPurpose', models.DO_NOTHING, blank=True, null=True)
    pay_acc_numb = models.ForeignKey(Card, models.DO_NOTHING, db_column='pay_acc_numb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purpose'


class ScholarshipPurpose(models.Model):
    scholarship_id = models.AutoField(primary_key=True)
    purpose_date = models.DateField()
    type = models.ForeignKey('ScholarshipType', models.DO_NOTHING, blank=True, null=True)
    student_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_code', blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_purpose'


class ScholarshipType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'scholarship_type'


class Student(models.Model):
    student_code = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    facultet_code = models.ForeignKey(Facultet, models.DO_NOTHING, db_column='facultet_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
