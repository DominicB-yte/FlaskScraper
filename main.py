from flask import Flask, render_template
import scraper
import json

#Define app
app = Flask(__name__)
trademe = "https://www.trademe.co.nz/gaming/playstation-4/consoles"

#Get list of articles
trademe_listings = scraper.process(scraper.scrape(trademe))
#print(nz_articles[0]["title"])

#Define Homepage
@app.route("/")
def home():
    return render_template("index.html", len=len(trademe_listings), listings=trademe_listings)

#Start app
if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
