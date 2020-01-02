import requests
import datetime
import bs4 as bs
from django.shortcuts import render
from .models import Company
from django.conf import settings
import matplotlib.pyplot as plt
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries
from django.http import HttpResponse

alpha_vantage_key = settings.ALPHAVANTAGE_API_KEY

class HomeView(TemplateView):
    template_name = 'stocks/index.html'
  
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tickers = []
        companies=Company.objects.filter(created_at=datetime.date.today())
        #if updated list of companies are already in the DB, there is no need to rescraping the website
        if companies:
            ctx["companies"] = Company.objects.all()
        else:
            # Either the 500 companies are not updated or the table is empty
            Company.objects.all().delete()
            #scraping this website updated regularly to get a list of 500 companies
            resp = requests.get("https://www.slickcharts.com/sp500")
            soup = bs.BeautifulSoup(resp.text,features="html.parser")
            table = soup.find('table',{'class':'table table-hover table-borderless table-sm'})
            for row in table.findAll('tr')[1:]:
                company_symbol = row.findAll('td')[2].text
                company_name = row.findAll('td')[1].text
                Company.objects.create(symbol =company_symbol, name =company_name)
                ctx["companies"] = Company.objects.all()
        return ctx


def GraphView(request,slug):
    ti = TimeSeries(key=alpha_vantage_key, output_format='pandas')
    data, meta_data = ti.get_daily(symbol=slug)
    data.plot()
    plt.title('Daily Times Series for the '+slug+ ' stock')
    plt.savefig('new-fig.png')
    image_data = open("new-fig.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
