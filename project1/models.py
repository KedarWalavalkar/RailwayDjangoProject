from django.db import models
from django.utils import timezone
# from django.core.files.storage import FileSystemStorage
class Users(models.Model):
    uname=models.CharField(max_length=30)
    upassword=models.CharField(max_length=30)
    
class category(models.Model):
    cat_id=models.IntegerField(max_length=50, primary_key=True)
    cat_name=models.CharField(max_length=500)

class desg(models.Model):
    desgID=models.IntegerField(max_length=50, primary_key=True)
    desgName=models.CharField(max_length=500)

class grievance(models.Model):
    grievanceID=models.IntegerField(max_length=50, primary_key=True)
    types=models.CharField(max_length=500)

class section(models.Model):
    sectionID=models.IntegerField(max_length=50,primary_key=True)
    sectionName=models.CharField(max_length=500)

class shop(models.Model):
    shopID=models.IntegerField(max_length=50,primary_key=True)
    shopName=models.CharField(max_length=500)

class uploads(models.Model):
    files=models.FileField(max_length=100)
    types=models.CharField(max_length=10)
    size=models.IntegerField(max_length=100)
    CR_NO=models.IntegerField(max_length=100)
    CR_DATE=models.DateField(auto_now=True)
    subject=models.CharField(max_length=255)
    RBE_NO=models.IntegerField()
    RBE_DT=models.DateField()

cat_choice=[
    ('notification','Notification'),
    ('circular','Circular'),
    ('sbf','SBF'),
    ('union','Union'),
    ('retirement','Retirement'),
    ('qb','Question Bank'),
]
class uploads_cat(models.Model):
    files=models.FileField(max_length=100)
    cwm_letter_no=models.CharField(max_length=255)
    cwm_letter_date=models.DateTimeField()
    subject=models.CharField(max_length=255)
    cat_name=models.CharField(max_length=255,choices=cat_choice,default='notification')
# shop=models.CharField(max_length=255,choices=shop_choice,default='fitter')


class uploads_gri(models.Model):
    files=models.FileField(max_length=100)
    cwm_letter_no=models.CharField(max_length=255)
    cwm_letter_date=models.DateField(auto_now=True)
    subject=models.CharField(max_length=255)
    types=models.CharField(max_length=255)
    sectionName=models.CharField(max_length=255)

shop_choice=[
    ('fitter','Fitter'),
    ('carpenter','Carpenter'),
    ('welder','Welder'),
    ('blacksmith','Blacksmith'),
    ('painter','Painter'),
    ('personnel','Personnel'),
    ('combined','Combined KH List'),
    ('milwright','Milwright'),
    ('trimmer','Trimmer'),
    ('machinist','Machinist'),
]
desg_choice=[
    ('sse','SSE'),
    ('je','JE'),
    ('sr.tech','Sr. Tech'),
    ('tech-i','Tech I'),
    ('tech-ii','Tech II'),
    ('tech-iii','Tech III'),
    ('khalasi','Khalashi'),
    ('ch.os','Ch. OS'),
    ('os','OS'),
    ('sr.clerk','Sr. Clerk'),
    ('jr.clerk','Jr. Clerk'),
    ('peon','Peon'),
]

class uploads_qb(models.Model):
    files=models.FileField(max_length=100)
    cwm_letter_no=models.CharField(max_length=255)
    cwm_letter_date=models.DateTimeField()
    subject=models.CharField(max_length=255)
    shop=models.CharField(max_length=255,choices=shop_choice,default='fitter')

class uploads_sl(models.Model):
    files=models.FileField(max_length=100,name='files')
    cwm_letter_no=models.CharField(max_length=255)
    cwm_letter_date=models.DateTimeField()
    subject=models.CharField(max_length=255)
    shop=models.CharField(max_length=255,choices=shop_choice,default='fitter')
    desg=models.CharField(max_length=255,choices=desg_choice,default='sse')
    # color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    
    def save(self, *args, **kwargs):
        self.cwm_letter_date = timezone.now()
        return super(uploads_sl, self).save(*args, **kwargs)