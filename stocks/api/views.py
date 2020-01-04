import requests
import bs4 as bs
import datetime
from rest_framework import generics
from stocks.models import Company
from .serializers import CompanySerializer

class StockAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



    def get_queryset(self):
        companies=Company.objects.filter(created_at=datetime.date.today())
        #if updated list of companies are already in the DB, there is no need to rescraping the website
        def scrap_website(companies):
            if not companies:
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
        scrap_website(companies)
        return self.queryset
