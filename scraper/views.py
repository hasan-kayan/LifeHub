from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import csv
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
# Create your views here.

def home(request):
    return render(request, "scraper/index.html")


def csv(request):
      
    return HttpResponse('CSV')

