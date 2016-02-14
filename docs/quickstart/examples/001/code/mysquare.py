from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def venues_list():
    return 'Venues list'

@app.route("/<venue_id>")
def venue_detail(venue_id):
    return 'Venue with id "%s"' % venue_id

if __name__ == "__main__":
    app.run(debug=True)
