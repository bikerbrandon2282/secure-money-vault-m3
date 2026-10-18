from django.db import models
from django.utils import timezone

# Create your models here.
type_choices = (
    (1, 'Income'),
    (2, 'Expense'),
)
currency_choices = (
    (1, 'British Pound'),
    (2, 'US Dollar'),
    (3, 'Euro'),
    (4, 'Japanese Yen'),
    (5, 'Indian Rupee'),
)
category_choices = (
    (1, 'Create New Category'),
    (2, 'Rent'),
    (3, 'Food'),
    (4, 'Transportation'),
    (5, 'Entertainment'),
    (6, 'Utilities'),
    (7, 'Healthcare'),
    (8, 'Education'),
    (9, 'Shopping'),
    (10, 'Travel'),
    (11, 'Other'),
)
class transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=type_choices, default=2)
    date = models.DateTimeField()
    currency = models.IntegerField(choices=currency_choices, default=1)
    category = models.IntegerField(choices=category_choices, default=1)
    description = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - Amount: {self.amount}"