from django.contrib import admin
from .models import Income, Expense, Token


admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Token)
