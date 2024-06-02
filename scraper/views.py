from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup


def index(request):
    data = ScrapedData.objects.all()
    return render(request, 'scraper/index.html', {'data': data})


def scrape(request):
    url = 'https://www.codewars.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='item')
    for item in items:
        title = item.find('h2').text
        link = item.find('a')['href']
        description = item.find('p').text

        ScrapedData.objects.create(
            title=title,
            link=link,
            description=description
        )

    return redirect('index')