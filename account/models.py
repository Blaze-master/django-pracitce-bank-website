from django.db import models

# Create your models here.
class UserAccount(models.Model):
    accountNo = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNo = models.IntegerField()
    email = models.EmailField()
    money = models.IntegerField(default=0)


class UserTransaction(models.Model):
    sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, primary_key=True, unique=False, related_name="%(class)s_sender")
    reciever = models.ForeignKey(UserAccount, on_delete=models.CASCADE, unique=False, related_name="%(class)s_reciever")
    timeSent = models.DateTimeField("Time sent")
    amount = models.IntegerField()