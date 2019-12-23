from flask import Flask, render_template


app = Flask(__name__)


app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
app.config['FREEZER_RELATIVE_URLS'] = True

HOSTING_DOMAIN = 'http://mdejongere.nl/'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/privacy.html")
def privacy():
    return render_template('privacy.html')


@app.route("/boek.html")
def boek():
    return render_template('boek.html')


@app.route("/pers.html")
def pers():
    return render_template('pers.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/ingeschreven.html")
def signed_up():
    return render_template('ingeschreven.html')


@app.route("/bevestigd.html")
def confirmed():
    return render_template('bevestigd.html')


@app.route("/uitgeschreven.html")
def signed_off():
    return render_template('uitgeschreven.html')


@app.route("/404.html")
def not_found():
    return render_template('404.html')


@app.route("/sitemap.xml")
def sitemap():
    return render_template('sitemap.xml')


@app.route("/robots.txt")
def robots():
    return """
    User-agent: *
    Sitemap: http://www.mdejongere.nl/sitemap.xml
    """

if __name__ == "__main__":
    app.run(debug=True)