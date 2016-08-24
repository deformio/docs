from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def venues_list():
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/',
        headers={
            'Authorization': 'Token TFWaTgjB'
        }
    )
    response.raise_for_status()
    return response.content

@app.route("/<venue_id>")
def venue_detail(venue_id):
    # retrieving a document by venue_id
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/%s/' % (
            venue_id,
        ),
        headers={
            'Authorization': 'Token TFWaTgjB'
        }
    )
    if response.status_code == 404:
        # if no document with venue_id then return 404 error
        return 'Venue with id "%s" is not found' % venue_id, 404
    else:
        response.raise_for_status()
        return response.content

if __name__ == "__main__":
    app.run(debug=True)
