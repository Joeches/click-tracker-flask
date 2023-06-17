from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

# Simulated click data
clicks_data = [
    {"date": "2023-06-15", "clicks": 100},
    {"date": "2023-06-16", "clicks": 150},
    {"date": "2023-06-17", "clicks": 120},
    # Add more data here...
]

@api.route('/clicks')
class Clicks(Resource):
    def get(self):
        total_clicks = sum(data['clicks'] for data in clicks_data)
        return {'total_clicks': total_clicks, 'clicks_data': clicks_data}

if __name__ == '__main__':
    app.run(debug=True)
