from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def venues_list():
    # make HTTP requests
    response = requests.get(
        'https://mysquare.deform.io/api/collections/venues/documents/'
    )
    # raise error if bad response code
    response.raise_for_status()
    # return raw content from the response
    return response.content

@app.route("/<venue_id>")
def venue_detail(venue_id):
    return 'Venue with id "%s"' % venue_id

if __name__ == "__main__":
    app.run(debug=True)
