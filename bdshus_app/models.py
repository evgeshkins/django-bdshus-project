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
    bank_name = models.CharField(max_length=50, verbose_name="Название банка")

    class Meta:
        managed = False
        db_table = 'bank'
        verbose_name = "Банк"
        verbose_name_plural = "Банки"

    def __str__(self):
        return f"Банк {self.bank_name}"

class Card(models.Model):
    pay_acc_numb = models.AutoField(primary_key=True)
    number_card = models.CharField(max_length=16, verbose_name="Номер банковской карты")
    bank_number = models.ForeignKey(Bank, models.DO_NOTHING, db_column='bank_number', blank=True, null=True, verbose_name="Номер банка")
    student_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_code', blank=True, null=True, verbose_name="Код студента")

    class Meta:
        managed = False
        db_table = 'card'
        verbose_name = "Банковская карта"
        verbose_name_plural = "Банковские карты"

    def __str__(self):
        return f"Банковская карта номер {self.number_card}"


class Division(models.Model):
    division_code = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=50, verbose_name="Название подразделения")

    class Meta:
        managed = False
        db_table = 'division'
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return f"Подразделение '{self.division_name}'"


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия работника")
    middle_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество работника")
    first_name = models.CharField(max_length=50, verbose_name="Имя работника")
    division_code = models.ForeignKey(Division, models.DO_NOTHING, db_column='division_code', blank=True, null=True, verbose_name="Код подразделения")

    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return f"Работник: {self.last_name} {self.first_name} {self.middle_name}"


class Facultet(models.Model):
    facultet_code = models.AutoField(primary_key=True)
    facultet_name = models.CharField(max_length=50, verbose_name="Название факультета")

    class Meta:
        managed = False
        db_table = 'facultet'
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def __str__(self):
        return f"{self.facultet_name}"


class Purpose(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    purpose_sum = models.FloatField(verbose_name="Сумма выплаты")
    purpose_date = models.DateField(verbose_name="Дата выплаты")
    scholarship = models.ForeignKey('ScholarshipPurpose', models.DO_NOTHING, blank=True, null=True, verbose_name="id назначения")
    pay_acc_numb = models.ForeignKey(Card, models.DO_NOTHING, db_column='pay_acc_numb', blank=True, null=True, verbose_name="Номер расчетного счета (карта)")

    class Meta:
        managed = False
        db_table = 'purpose'
        verbose_name = "Выплата"
        verbose_name_plural = "Выплаты"

    def __str__(self):
        return f"Выплата: сумма - {self.purpose_sum}, дата - {self.purpose_date}"


class ScholarshipPurpose(models.Model):
    scholarship_id = models.AutoField(primary_key=True)
    purpose_date = models.DateField(verbose_name="Дата назначения")
    type = models.ForeignKey('ScholarshipType', models.DO_NOTHING, blank=True, null=True, verbose_name="id вида стипендии")
    student_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_code', blank=True, null=True, verbose_name="Код студента")
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True, verbose_name="id сотрудника")

    class Meta:
        managed = False
        db_table = 'scholarship_purpose'
        verbose_name = "Назначение стипендии"
        verbose_name_plural = "Назначения стипендий"

    def __str__(self):
        return f"Назначение стипендии от {self.purpose_date}"


class ScholarshipType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, verbose_name="Название вида стипендии")

    class Meta:
        managed = False
        db_table = 'scholarship_type'
        verbose_name = "Вид стипендии"
        verbose_name_plural = "Виды стипендий"

    def __str__(self):
        return f"{self.type_name}"


class Student(models.Model):
    student_code = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    facultet_code = models.ForeignKey(Facultet, models.DO_NOTHING, db_column='facultet_code', blank=True, null=True, verbose_name="Код факультета")

    class Meta:
        managed = False
        db_table = 'student'
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"Студент: {self.last_name} {self.first_name} {self.middle_name}"