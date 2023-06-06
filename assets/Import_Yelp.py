import requests
import json
import pandas as pd
import openpyxl

#Define business ID
business_id = 'Restaurants'

#Define API Key, Endpoint, and Header
API_KEY = 'Your API Key'
BUSINESS_PATH = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define the Parameters of the search
PARAMETERS = {'location':'Barcelona',
              'latitude': 41.383860, 
              'longitude': 2.173766,
              'term': 'Restaurant',
              'limit': 50,
              'radius': 500,
              'categories': 'bars',
              'attributes': 'outdoor_seating'}

# Make a Request to the API, and return results
response = requests.get(url=BUSINESS_PATH, 
                        params=PARAMETERS, 
                        headers=HEADERS)

# Convert response to a JSON String
business_data = response.json()  

# # print the data
# print(json.dumps(business_data, indent = 3))

#Convert JSON to a Pandas DataFrame
df = pd.DataFrame.from_dict(business_data['businesses'])
#print(df)

# Write data to an Excel File
df.to_excel('data.xlsx', sheet_name='Sheet1')

#Extract all the Business ID from the JSON Response
business_ids = [business['id'] for business in business_data['businesses']]


#Make request to the API Business Endpoint to get reviews
reviews_data = []

for business_id in business_ids:
    response = requests.get(url=f'https://api.yelp.com/v3/businesses/{business_id}/reviews', headers=HEADERS)
    reviews_data.append(response.json())

# print the data
#print(json.dumps(reviews_data, indent = 3))





#Convert JSON to a Pandas DataFrame
df_r = pd.DataFrame.from_dict(reviews_data)
#print(df_r)




# #Extract first column and row of the DataFrame
# df_r = df_r.iat[1,1]

# df_r_split = df_r.split(',')

# print(df_r_split)



#Write data to an Excel File
df_r.to_excel('data_reviews.xlsx', sheet_name='Sheet1')


