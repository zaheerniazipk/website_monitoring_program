# Project: Website Monitoring Program

# Install the requests package using cmd
# pip install requests

# import the  requests package for HTTP requests
import requests

# import the time module
import time


while True:
    print("\n************** Website Monitoring Program ************\n")

    # Website URL
    url = input("Enter website URL: ")

    response = requests.get(url)
    web_status = response.status_code

    # Status code 200 Ok Response (standard response for successful HTTP requests)
    if web_status != 200:
        print("\nStatus Code: ", web_status)
        print(f"The website: {url} is not working fine!\n")

        # Recommendations
        print("\nRecommendations: ")
        print("1.Need to check your internet connection")
        print("2.Need to check your browser")
        print("3.Need to check your website")
        break

    else:
        print("\nStatus Code: ", web_status)
        print(f"The website: {url} is working fine!\n")
        continue

    # Re-run Program after secs
    time.sleep(3)
