from django.db import models




class Dealer(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    address = models.TextField(default='', verbose_name='Address')
    contact = models.IntegerField(blank=False, null=False, verbose_name='Contacts')
    worker_hours = models.TextField(default='', verbose_name='Worker hours')

    def __str__(self):
        return self.title




class Car(models.Model):
    brand = models.CharField(max_length=20)
    dealer = models.ManyToManyField(Dealer, related_name='dealers')

    def __str__(self):
        return self.brand

    def dealer_display(self):
        return ', '.join([dealer.title for dealer in self.dealer.all()])

    dealer_display.short_descriptions = 'Dealer'



