from django.db import models
from django.contrib.auth.models import User
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
    (1, 'Select An Option'),
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


def generate_transaction_id():
    '''
    Generates a Transaction ID for the user using the models Primary key
    '''
    last = Transaction.objects.order_by('-id').first()

    if last:
        # Extract the numeric part
        last_num = int(last.transaction_id)
        new_num = last_num + 1
    else:
        new_num = 1

    return f"{new_num:04d}"   # formats 0 → "0000", 12 → "0012"


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'budget_user')
    transaction_id = models.CharField(max_length=100, default = generate_transaction_id ,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=type_choices, default=2)
    date = models.DateTimeField(default=timezone.now)
    category = models.IntegerField(choices=category_choices, default=1)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Transaction {self.transaction_id} - Amount: {self.amount}"

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    currency = models.IntegerField(choices=currency_choices, default=1)

    @property
    def currency_symbol(self):
        symbols = {
            1: '£',
            2: '$',
            3: '€',
            4: '¥',
            5: '₹',
        }
        return symbols.get(self.currency, '£')