from django.contrib import admin
from .models import Book, Customer, Loan

admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Loan)
