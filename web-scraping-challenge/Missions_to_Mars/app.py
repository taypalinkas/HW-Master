from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# client = PyMongo.MongoClient()
#db = client.mars_db
#collection = db.mars_web

@app.route("/")
def home():
    mars = list(db.mars_web.find())
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
	mars_data = scrape_mars.scrape_info()

	mongo.db.collecton.update({}, mars_data, upsert=True)

	return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)