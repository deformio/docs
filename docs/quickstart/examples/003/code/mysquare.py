from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def venues_list():
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/',
        # use authorization token
        headers={
            'Authorization': 'Token TFWaTgjB'
        }
    )
    response.raise_for_status()
    return response.content

@app.route("/<venue_id>")
def venue_detail(venue_id):
    return 'Venue with id "%s"' % venue_id

if __name__ == "__main__":
    app.run(debug=True)
