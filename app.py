from flask import Flask, request, jsonify
from datetime import datetime
from collections import OrderedDict

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Disable sorting of JSON keys

@app.route('/')
def index():
    # Get the query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get the current UTC time
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Create the response data as an OrderedDict
    data = OrderedDict([
        ('slack_name', slack_name),
        ('current_day', current_day),
        ('utc_time', utc_time),
        ('track', track),
        ('github_file_url', 'https://github.com/BUSOLA12/my_HNGx_project_1/blob/main/app.py'),
        ('github_repo_url', 'https://github.com/BUSOLA12/my_HNGx_project_1.git'),
        ('status_code', 200)
    ])

    # Return the JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run()
