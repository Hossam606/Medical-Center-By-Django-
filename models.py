from django.db import models

# Create your models here.
Time_Selection=(
            ("04.00 pM to 07.00 PM", "04.00 AM to 07.00 PM"),
            ("07.00 AM to 10.00 PM", "07.00 AM to 10.00 PM"),
)
DAY_SELECTION = (
            ("Satarday", "Satarday"),
            ("Sunday", "Sunday"),
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
             
        )


class Department(models.Model):
    name=models.CharField(max_length=50)
    photo= models.ImageField(upload_to='photo',null=True,blank=True)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=40)
    description =models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photo',null=True,blank=True)
    Date=models.CharField(max_length=50,null=True,blank=True,choices=DAY_SELECTION)
    Time=models.CharField(max_length=50,null=True,blank=True,choices=Time_Selection)
    Department=models.ForeignKey(Department,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    your_name=models.CharField(max_length=30)
    your_email=models.CharField(max_length=50)
    subject=models.CharField(max_length=20)
    your_message=models.TextField()
    def __str__(self):  
        return self.your_name

class Registration(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    Doctor_name=models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True,blank=True)
    Date=models.CharField(max_length=50,null=True,blank=True,choices=DAY_SELECTION)
    Time=models.CharField(max_length=50,null=True,blank=True,choices=Time_Selection)
    def __str__(self):
        return self.name



#class Appointment(models.Model):
   # First_Name=models.CharField(max_length=30)
    #Last_name=models.CharField(max_length=40)
    #Phone=models.IntegerField(null=True,blank=True)
    #Doctors=models.CharField(max_length=50,null=True,blank=True)
    #Doctors=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    #Data=models.DateField()
    #Time=models.TimeField(null=True)
    #def __str__(self):
     #   return self.First_Name

 


 