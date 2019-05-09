from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"]="mongodb://localhost:27017/app.py"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

    # # Find one record of data from the mongo database
    # destination_data = mongo.db.collection.find_one()

    # # Return template and data
    # return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_mars_news
    mars_data = scrape_mars.scrape_mars_image
    mars_data = scrape_mars.scrape_mars_facts
    mars_data = scrape_mars.scrape_mars_weather
    mars_data = scrape_mars.scrape_mars_hemispheres
    mars.update({}, mars_data,upsert=True)
    
    # scrape_costa.scrape_info()
    # # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
