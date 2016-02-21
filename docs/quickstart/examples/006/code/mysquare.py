from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

# store token value in a variable
TOKEN = 'TFWaTgjB'

@app.route("/")
def venues_list():
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/',
        headers={
            # reuse the variable
            'Authorization': 'Token %s' % TOKEN
        }
    )
    response.raise_for_status()
    return render_template(
        'venues_list.html',
        venues=response.json()['result']
    )

@app.route("/<venue_id>")
def venue_detail(venue_id):
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/%s/' % (
            venue_id,
        ),
        headers={
            # reuse the variable
            'Authorization': 'Token %s' % TOKEN
        }
    )
    if response.status_code == 404:
        return 'Venue with id "%s" is not found' % venue_id, 404
    else:
        response.raise_for_status()
        return render_template(
            'venue_detail.html',
            venue=response.json()['result'],
            # send token to the template
            token=TOKEN
        )

if __name__ == "__main__":
    app.run(debug=True)
