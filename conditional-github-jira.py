import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask , request

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():
    webhook = request.json
    comment = webhook['comment']['body']

    if "/jira" in comment:
        url = "https://manogna.atlassian.net/rest/api/3/issue"

        API_TOKEN=""

        auth = HTTPBasicAuth("manogna@gmail.com", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps( {
            "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                        }
                    ],
                "type": "doc",
                "version": 1
            },
            "project": {
            "key": "MA"
            },
            "issuetype": {
                "id": "10004"
            },
            "summary": "Main order flow broken",
        },
        "update": {}
        } )


        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Jira issue will be created if the comment includes /jira"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
