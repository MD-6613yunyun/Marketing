# This excel workbook is scraping the car workshop shop websites and 
# extract all the infomations and import into excel
import requests
from bs4 import BeautifulSoup
import csv

# Set the URL
base_url = 'https://www.automobiledirectory.com.mm/vehicle-spare-parts'
base_url = 'https://www.automobiledirectory.com.mm/vehicle-spare-parts/p:'
base_url = "https://www.automobiledirectory.com.mm/k:Car+Spa+%2526+Painting+Service/p:"
base_url = "https://www.automobiledirectory.com.mm/listing/body-paint-workshops/p:"
# set the num of page
num_pages = 23

# Create an empty list to store the movie data
shops = []

for page_no in range(2,num_pages+1):
    # Loop through each page of the website and scrape the movie data
    # for page in range(2, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page_no)
    # Send a request to the website and get the HTML response
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the movie listings on the page
    listings = soup.find_all('div', class_='summary-info')

    # Loop through each movie listing and extract the data
    for listing in listings:
        try:
            name = listing.find('a',class_="heading h-4 title").text.strip()
        except:
            name = "Not Assigned"
        try:
            category = listing.find('address',class_="summary-address").text.strip()
        except:
            category = "Not Assigned"
        try:
            address = listing.find_all_next('address',class_="summary-address")
        except:
            address = listing.find_all_next('address',class_="summary-address")
        try:
            contact = listing.find('div', class_="summary-phone").text.strip()
        except:
            contact = "Not Assigned"
        try:
            ward = address[1].text.strip().replace("\n"," ").split(",,")[0].strip()
        except:
            ward = "Not Assigned"
        try:
            township = address[1].text.strip().replace("\n"," ").split(",,")[1].strip().split(",")[0]
            city = address[1].text.strip().replace("\n", " ").split(",,")[1].strip().split(",")[1].strip()
        except:
            township = address[1].text.strip().replace("\n", " ").split(",,")
            city = address[1].text.strip().replace("\n", " ").split(",,")
        phone = contact.split(" ")[0] if len(contact.split(" ")) > 1 else contact.split(" ")[0] + "," + contact.split(" ")[-1]

        # print(address[1].text.strip().replace("\n"," ").split(",,")[0].strip())
        # print(address[1].text.strip().replace("\n"," ").split(",,")[1].strip().split(",")[0])
        # print(address[1].text.strip().replace("\n"," ").split(",,")[1].strip().split(",")[1].strip())
        # Add the movie data to the list
        shops.append({'Dealer Name': name,'Category':category,'Ward':ward,'Township':township,'City':city,'Phone':phone})
# Save the movie data to a CSV file
file_path = "D:\\MDMM Test files\\Marketing\\car_paintings_shop.csv"
with open(file_path, 'a', newline='',encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Dealer Name','Category','Ward','Township','City','Phone'])
    writer.writeheader()
    writer.writerows(shops)
