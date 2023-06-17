from flask import Flask
from flask_restx import Api, Resource
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)
api = Api(app)

# Define your Google Analytics credentials file path
credentials_file = 'path/to/your/credentials.json'

# Define your Google Analytics View ID
view_id = 'your-view-id'

# Create a service object for making Google Analytics API requests
credentials = service_account.Credentials.from_service_account_file(credentials_file)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

@api.route('/clicks')
class Clicks(Resource):
    def get(self):
        # Make a request to the Google Analytics API to fetch click data
        response = analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': view_id,
                        'dateRanges': [{'startDate': '2023-06-15', 'endDate': '2023-06-17'}],
                        'metrics': [{'expression': 'ga:totalEvents'}],
                        'dimensions': [{'name': 'ga:date'}]
                    }
                ]
            }
        ).execute()

        # Parse the response to extract click data
        data = response['reports'][0]['data']['rows']
        clicks_data = [{'date': row['dimensions'][0], 'clicks': int(row['metrics'][0]['values'][0])} for row in data]
        total_clicks = sum(row['clicks'] for row in clicks_data)

        return {'total_clicks': total_clicks, 'clicks_data': clicks_data}

if __name__ == '__main__':
    app.run(debug=True)
