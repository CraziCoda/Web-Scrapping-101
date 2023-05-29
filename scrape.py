# Import the libraries need 
import requests
from bs4 import BeautifulSoup
import csv


#Take user input for the search term
search_term=input("Enter the search term: ")

# make requests to the website
response = requests.get(f"https://jiji.com.gh/search?query={search_term}")

