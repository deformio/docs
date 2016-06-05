from flask import Flask
from flask import render_template
# flask request object
from flask import request
import requests

app = Flask(__name__)

TOKEN = 'TFWaTgjB'

@app.route("/")
def venues_list():
    # get search text
    search_text = request.args.get('search')
    if search_text:
        # search documents if search query
        response = requests.post(
            'https://mysquare.deform.io/api/collections/venues/documents/',
            headers={
                'Authorization': 'Token %s' % TOKEN,
                'X-Action': 'find'
            },
            json={
                'payload': {
                    'text': search_text
                }
            }
        )
    else:
        # get all documents if no search query
        response = requests.get(
            'https://mysquare.deform.io/api/collections/venues/documents/',
            headers={
                'Authorization': 'Token %s' % TOKEN
            }
        )
    response.raise_for_status()
    return render_template(
        'venues_list.html',
        venues=response.json()['result']['items'],
        # send search_text to template
        search_text=search_text
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
