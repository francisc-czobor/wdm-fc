from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from .models import Book, Customer, Loan
from .forms import BookForm


def ceva(request):
    return HttpResponse('Ceva')


def home(request):
    context = {
        'chestie': timezone.now().microsecond,
    }
    return render(request, template_name='home.html', context=context)


def tabele(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = Book(
                title=str(form.cleaned_data['title']),
                author=str(form.cleaned_data['author']),
                issue_date=str(form.cleaned_data['issue_date']),
                pages_no=str(form.cleaned_data['pages_no']),
            )

            book.save()
        else:
            print('tzeapa')

    books = Book.objects.all().order_by('title')
    customers = Customer.objects.all()
    loans = Loan.objects.all()

    books_borrowed_by_franci = Book.objects.filter(loans__customer__name='Francisc Czobor')

    book_form = BookForm()

    context = {
        'books': books,
        'customers': customers,
        'loans': loans,
        'bbbf': books_borrowed_by_franci,
        'book_form': book_form,
    }

    return render(request, template_name='tabele.html', context=context)
