from flask import Flask
# function for rendering templates
from flask import render_template
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
    # render venues_list.html template
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
            'Authorization': 'Token TFWaTgjB'
        }
    )
    if response.status_code == 404:
        return 'Venue with id "%s" is not found' % venue_id, 404
    else:
        response.raise_for_status()
        # render venue_detail.html template
        return render_template(
            'venue_detail.html',
            venue=response.json()['result']
        )

if __name__ == "__main__":
    app.run(debug=True)
