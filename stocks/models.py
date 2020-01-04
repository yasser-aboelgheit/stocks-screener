from django.db import models
from django.urls import reverse,reverse_lazy
from django.contrib.sites.models import Site
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    created_at =  models.DateField(auto_now_add=True)
    graph = models.URLField()

    def __str__(self):
        return self.name+" - "+self.symbol

    def save(self, *args, **kwargs):
        domain=Site.objects.get_current().domain
        if settings.DEBUG:
            self.graph = "http://localhost:8000"+str(reverse_lazy("stocks:graph",kwargs={"slug":self.symbol}))
        else:
            self.graph =str(domain) +str(reverse_lazy("stocks:graph",kwargs={"slug":self.symbol}))
        super(Company, self).save(*args, **kwargs) 