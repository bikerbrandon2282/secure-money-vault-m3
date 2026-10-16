from django.db import models

# Create your models here.
type_choices = (
    (1, 'Income'),
    (2, 'Expense'),
)
currency_choices = (
    (1, 'US Dollar'),
    (2, 'Euro'),
    (3, 'British Pound'),
    (4, 'Japanese Yen'),
    (5, 'Indian Rupee'),
)
class transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=type_choices, default=2)
    date = models.DateTimeField(auto_now_add=True)
    currency = models.IntegerField(choices=currency_choices, default=3)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - Amount: {self.amount}"