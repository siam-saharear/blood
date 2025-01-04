# from django.db import models

# # Create your models here.



# class Organ_systems(models.Model):
#     organ_system = models.CharField(max_length=19)
#     def __str__(self):
#         return self.organ_system

# class Organs(models.Model):
#     organ_name = models.CharField(max_length=29)
#     organ_function = models.CharField(max_length=1000)
#     organ_system = models.ForeignKey(Organ_systems, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.organ_name
    
#     def save(self, *args, **kwargs):
#         if self.pk is None:
#             self.id = self.get_next_id()
#         super().save(*args, **kwargs)

#     def get_next_id(self):
#         # Find the smallest available ID
#         used_ids = set(Organs.objects.values_list('id', flat=True))
#         all_ids = set(range(1, max(used_ids, default=0) + 2))
#         available_ids = sorted(all_ids - used_ids)
#         return available_ids[0] if available_ids else max(used_ids, default=0) + 1
    
    
    

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AggriculturalOfficer(models.Model):
    aid = models.OneToOneField('User', models.DO_NOTHING, db_column='AID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aggricultural_officer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DidPidRidNid(models.Model):
    did = models.OneToOneField('User', models.DO_NOTHING, db_column='did', primary_key=True)  # The composite primary key (did, pid, rid, nid) found, that is not supported. The first column is selected.
    pid = models.IntegerField()
    rid = models.IntegerField()
    nid = models.ForeignKey('User', models.DO_NOTHING, db_column='nid', related_name='didpidridnid_nid_set')

    class Meta:
        managed = False
        db_table = 'did_pid_rid_nid'
        unique_together = (('did', 'pid', 'rid', 'nid'),)


class DinsributorCompany(models.Model):
    did = models.OneToOneField('User', models.DO_NOTHING, db_column='DID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dinsributor_company'


class Distributorcompanydemand(models.Model):
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pid = models.OneToOneField('Product', models.DO_NOTHING, db_column='PID', primary_key=True)  # Field name made lowercase. The composite primary key (PID, DID) found, that is not supported. The first column is selected.
    did = models.ForeignKey(DinsributorCompany, models.DO_NOTHING, db_column='DID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distributorcompanydemand'
        unique_together = (('pid', 'did'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Farmer(models.Model):
    fid = models.OneToOneField('User', models.DO_NOTHING, db_column='FID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farmer'


class Harvest(models.Model):
    harvest_id = models.AutoField(db_column='Harvest_Id', primary_key=True)  # Field name made lowercase.
    crop_type = models.CharField(max_length=255, blank=True, null=True)
    hd = models.IntegerField(db_column='HD', blank=True, null=True)  # Field name made lowercase.
    hm = models.IntegerField(db_column='HM', blank=True, null=True)  # Field name made lowercase.
    hy = models.IntegerField(db_column='HY', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hcity = models.CharField(db_column='Hcity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    harea = models.CharField(db_column='Harea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hstreet = models.CharField(db_column='Hstreet', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvest'


class Neutroshonist(models.Model):
    nid = models.OneToOneField('User', models.DO_NOTHING, db_column='NID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'neutroshonist'


class Product(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    pfastname = models.CharField(db_column='PFastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plastname = models.CharField(db_column='PLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nid = models.ForeignKey(Neutroshonist, models.DO_NOTHING, db_column='NID', blank=True, null=True)  # Field name made lowercase.
    exday = models.IntegerField(db_column='ExDay', blank=True, null=True)  # Field name made lowercase.
    exm = models.IntegerField(db_column='ExM', blank=True, null=True)  # Field name made lowercase.
    exy = models.IntegerField(db_column='ExY', blank=True, null=True)  # Field name made lowercase.
    tem = models.DecimalField(db_column='TEM', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    humidity = models.DecimalField(db_column='Humidity', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    harvestid = models.ForeignKey(Harvest, models.DO_NOTHING, db_column='HarvestID', blank=True, null=True)  # Field name made lowercase.
    fid = models.ForeignKey(Farmer, models.DO_NOTHING, db_column='FID', blank=True, null=True)  # Field name made lowercase.
    aid = models.ForeignKey(AggriculturalOfficer, models.DO_NOTHING, db_column='AID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class ProductNutrition(models.Model):
    pid = models.OneToOneField(Product, models.DO_NOTHING, db_column='PID', primary_key=True)  # Field name made lowercase. The composite primary key (PID, vitamin, amount) found, that is not supported. The first column is selected.
    vitamin = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'product_nutrition'
        unique_together = (('pid', 'vitamin', 'amount'),)


class Productbuydistributorcompany(models.Model):
    pid = models.OneToOneField(Product, models.DO_NOTHING, db_column='PID', primary_key=True)  # Field name made lowercase. The composite primary key (PID, DID) found, that is not supported. The first column is selected.
    did = models.ForeignKey(DinsributorCompany, models.DO_NOTHING, db_column='DID')  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productbuydistributorcompany'
        unique_together = (('pid', 'did'),)


class Resultnutritionvalue(models.Model):
    resultid = models.OneToOneField('Samplingresult', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase. The composite primary key (ResultID, VITAMIN, AMOUNT) found, that is not supported. The first column is selected.
    vitamin = models.CharField(db_column='VITAMIN', max_length=100)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultnutritionvalue'
        unique_together = (('resultid', 'vitamin', 'amount'),)


class Samplingresult(models.Model):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='PID', blank=True, null=True)  # Field name made lowercase.
    resultid = models.AutoField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    ed = models.IntegerField(db_column='ED', blank=True, null=True)  # Field name made lowercase.
    em = models.IntegerField(db_column='EM', blank=True, null=True)  # Field name made lowercase.
    ey = models.IntegerField(db_column='EY', blank=True, null=True)  # Field name made lowercase.
    humidity = models.DecimalField(db_column='Humidity', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temptostore = models.DecimalField(db_column='TempToStore', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    resultsali = models.CharField(db_column='ResultSaLi', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rminute = models.IntegerField(db_column='RMinute', blank=True, null=True)  # Field name made lowercase.
    rhour = models.IntegerField(db_column='RHour', blank=True, null=True)  # Field name made lowercase.
    rday = models.IntegerField(db_column='RDay', blank=True, null=True)  # Field name made lowercase.
    rmonth = models.IntegerField(db_column='RMonth', blank=True, null=True)  # Field name made lowercase.
    ryear = models.IntegerField(db_column='RYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingresult'


class UseContactEmail(models.Model):
    uid = models.OneToOneField('User', models.DO_NOTHING, db_column='uid', primary_key=True)  # The composite primary key (uid, email_addresses) found, that is not supported. The first column is selected.
    email_addresses = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'use_contact_email'
        unique_together = (('uid', 'email_addresses'),)


class UseContactNumber(models.Model):
    uid = models.OneToOneField('User', models.DO_NOTHING, db_column='uid', primary_key=True)  # The composite primary key (uid, contact_number) found, that is not supported. The first column is selected.
    contact_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'use_contact_number'
        unique_together = (('uid', 'contact_number'),)


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    utype = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Wirehousemanager(models.Model):
    wid = models.OneToOneField(User, models.DO_NOTHING, db_column='WID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wirehousemanager'