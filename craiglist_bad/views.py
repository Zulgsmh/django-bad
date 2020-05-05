from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
import requests
from bs4 import BeautifulSoup
from . import models


BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMG_URL = 'https://images.craiglist.org/{}_300x300.jpg'


# Create your views here.   
def home(request):
    return render(request, 'craiglist_bad/index.html')


def new_search(request):
    """
    - get le texte de la recherche
    - Creation de la recherche qu'on insère dans la bdd
    - récupère url de base + la recherche
    - récupère le code source de la page
    - code source au format text
    """
    search = request.POST.get('search')
    obj = models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text

    #start to scrap elements
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    #initialisation tab final
    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            #0 pour avoir une seule image
            # split pour couper la string data ids en 3 car la première partie = id de la première image
            post_img_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_img_url = BASE_IMG_URL.format(post_img_id)
            print(post_img_url)
        else:
            post_img_url = 'https://craiglist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_img_url))


    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'craiglist_bad/new_search.html', stuff_for_frontend)
