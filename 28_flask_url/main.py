from flask import Flask  , render_template
 
# app = Flask(__name__,static_url_path="/pubic") # this is s how you change static url path

app = Flask(__name__, static_folder="assets", static_url_path="/public")  # this is how you change static folder and url path
@app.route("/")
def hello_world():
    return render_template("index.html")
app.run(port = 8000 ,debug=True)