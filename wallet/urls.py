from django.urls import path
from .views import submit_expense, submit_income, register


app_name = "wallet"

urlpatterns = [

	path("submit/expense/", submit_expense, name="submit_expense"),
	path("submit/income/", submit_income, name='submit_income'),
	path("accounts/register/", register, name='register'),
	# path("", views.index, name='index'),

	]