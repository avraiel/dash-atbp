# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowerca.
    employeelastname = models.CharField(db_column='EmployeeLastName', max_length=50)  # Field name made lowercase.
    employeefirstname = models.CharField(db_column='EmployeeFirstName', max_length=50)  # Field name made lowercase.
    employeemiddlename = models.CharField(db_column='EmployeeMiddleName', max_length=50)  # Field name made lowercase.
    startedroleon = models.DateTimeField(db_column='StartedRoleOn')  # Field name made lowercase.
    endedroleon = models.DateTimeField(db_column='EndedRoleOn', blank=True, null=True)  # Field name made lowercase.
    employeestatus = models.CharField(db_column='EmployeeStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'employee'


class Skill(models.Model):
    skillid = models.IntegerField(db_column='SkillID', primary_key=True)  # Field name made lowercase.
    addedby = models.ForeignKey(Employee, models.CASCADE, db_column='AddedBy')  # Field name made lowercase.
    skillname = models.CharField(db_column='SkillName', max_length=100)  # Field name made lowercase.
    skilltype = models.CharField(db_column='SkillType', max_length=50)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    deletedon = models.DateTimeField(db_column='DeletedOn', blank=True, null=True)  # Field name made lowercase.
    skillstatus = models.CharField(db_column='SkillStatus', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'skill'


class SkillLevel(models.Model):
    skilllevelid = models.IntegerField(db_column='SkillLevelID', primary_key=True)  # Field name made lowercase.
    skillid = models.ForeignKey(Skill, models.DO_NOTHING, db_column='SkillID')  # Field name made lowercase.
    addedby = models.ForeignKey(Employee, models.DO_NOTHING, db_column='AddedBy')  # Field name made lowercase.
    skilllevelvalue = models.IntegerField(db_column='SkillLevelValue')  # Field name made lowercase.
    skillleveldescription = models.CharField(db_column='SkillLevelDescription', max_length=500)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    editedon = models.DateTimeField(db_column='EditedOn')  # Field name made lowercase.
    deletedon = models.DateTimeField(db_column='DeletedOn', blank=True, null=True)  # Field name made lowercase.
    skilllevelstatus = models.CharField(db_column='SkillLevelStatus')  # Field name made lowercase.

    class Meta:
        db_table = 'skill_level'
