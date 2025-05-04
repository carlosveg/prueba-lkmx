from django.db import models


# Create your models here.


class WalletModel(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        #     managed = False  # Django no intentará crear ni migrar esta tabla
        db_table = 'wallets'  # Asegúrate que el nombre coincide con la tabla real
