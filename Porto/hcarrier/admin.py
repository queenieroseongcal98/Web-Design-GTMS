from django.contrib import admin
from hcarrier.models import Feedback, Transactions, Payment



# Register your models here.
admin.site.register(Feedback)
admin.site.register(Transactions)
admin.site.register(Payment)