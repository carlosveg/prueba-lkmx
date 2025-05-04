from django.db import models


# Create your models here.


class WalletModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        #     managed = False
        db_table = 'wallets'
