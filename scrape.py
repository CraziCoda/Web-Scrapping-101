# Import the libraries need 
import requests
from bs4 import BeautifulSoup
import csv


# Take user input for the search term
search_term=input("Enter the search term: ")

# make requests to the website
response = requests.get(f"https://jiji.com.gh/search?query={search_term}")

# getting a beautifulsoup object
soup = BeautifulSoup(response.text, "html.parser")



# getting all matching elements
containers = soup.select("div.b-list-advert__item-wrapper--base")




# array to store the results

results = []

# each container represent the "div.masonry-item" in the html
for container in containers:
    image = container.select_one("picture > img") # this finds the img tag within the picture tag
    image_link = image["src"] # this gets the src attribute of the image tag

    price_tag = container.select_one("div.qa-advert-price")  # this selects the tag containing the price data
    price = price_tag.text.strip() # this returns the text within the tag. The price

    name_tag = container.select_one('div.b-advert-title-inner')
    name = name_tag.text.strip() # this returns the text within the tag (div.b-advert-title-inner) which is the product name

    # .strip() removes leading and trailing spaces from the text making it more cleaner

    print(name, price, image_link)
    results.append({'Product Name': name, 'Product Price': price, 'Image': image_link}) 
    # The above adds a dict containing the info to results array 


with open("output.csv", "w") as file: # create and open a file called output.csv
    fieldnames = ['Product Name', 'Product Price', 'Image'] # Give headers of the csv file

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() # add header to csv
    writer.writerows(results) # add the data to the csv
