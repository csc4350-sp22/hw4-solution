import flask

app = flask.Flask(__name__)
SHOWS = [
    "Bojack Horseman",
    "Black Mirror",
    "I Think You Should Leave",
    "Haikyuu",
    "Scrubs",
]
IMAGES = [
    "/static/bojack.jpg",
    "/static/black_mirror.jpg",
    "/static/i_think.jpg",
    "/static/haikyuu.jpg",
    "/static/Scrubs.jpg",
]

@app.route("/")
def index():
    return flask.render_template(
        "index.html",
        length=len(SHOWS),
        shows=SHOWS,
        images=IMAGES,
    )

app.run(debug=True)