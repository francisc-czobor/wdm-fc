from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    issue_date = models.DateField()
    pages_no = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ''.join([self.title, ' de ', self.author])


class Customer(models.Model):
    name = models.CharField(max_length=32)
    dob = models.DateField()
    tel = models.CharField(max_length=13)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_date = models.DateField()

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ''.join([str(self.customer), ' - ', str(self.book)])
