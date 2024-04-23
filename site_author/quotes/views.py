from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.
from .utils import get_mongodb
from .models import Author
from .templatetags .extract import get_author


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def description_auth(request):
    db = get_mongodb()
    auth = db.authors.find()
    return render(request, template_name='quotes/descript_author.html', context={"auth": auth})
