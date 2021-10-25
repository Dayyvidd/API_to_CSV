import requests
import csv

# URL to the api we want to get information from
api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Headers dictionary containing API key necessary to access data
headers = {
    "X-CMC_PRO_API_KEY": "####### API KEY HERE #######"
}
# Using the request module get the information from the provided URL and header information
request = requests.get(url=api_url, headers=headers)

# Format the information in a JSON format (provided as a method of the requests module)
json = request.json()

# These exception items contain either list or dictionary items that would "complicate" our excel sheet
exceptions = ["tags", "quote", "platform"]
# Gathering field names into a list to use further down in the code
fieldnames = [key for key, value in json["data"][0].items() if key not in exceptions]

# Open csv file
with open("test_csv.csv", "w", newline="") as csv_file:
    # Initializing the DictWriter object passing it the open file handle, fieldnames and ignoring any extra fieldnames
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore",)
    # Write the headings on the first line of the sheet
    writer.writeheader()
    # Loop through each data point in the json dictionary each time writing a row with that data points values
    # for the corresponding column heading
    for i in range(len(json["data"])):
        writer.writerow(json["data"][i])
