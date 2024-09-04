from django.db import models

class InvoiceItem(models.Model):
    item_name = models.CharField(max_length=255)
    weight_pounds = models.FloatField()
    karat = models.FloatField()
    amount_gold = models.FloatField()

    def _str_(self):
        return f"Item {self.id}: {self.weight_pounds} lb, {self.karat} kt, GHS{self.amount_gold}"
