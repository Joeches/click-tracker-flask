import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define the base URL for your Flask API
base_url = 'http://localhost:5000'

# Define the API endpoint for retrieving click data
clicks_endpoint = '/clicks'

# Make a request to the API to fetch click data
response = requests.get(base_url + clicks_endpoint)
data = response.json()

# Extract the total clicks and clicks data from the response
total_clicks = data['total_clicks']
clicks_data = pd.DataFrame(data['clicks_data'])

# Create the Streamlit UI
st.title("Click Analytics Dashboard")
st.subheader("Total Clicks")
st.write(total_clicks)

st.subheader("Clicks Data")
st.dataframe(clicks_data)

# Create a line chart of the clicks over time using matplotlib
fig, ax = plt.subplots()
ax.plot(clicks_data['date'], clicks_data['clicks'])
ax.set_xlabel('Date')
ax.set_ylabel('Clicks')
ax.set_title('Clicks Over Time')
plt.xticks(rotation=45)
st.pyplot(fig)
