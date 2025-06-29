from flask import Flask  , render_template
 
app = Flask(__name__)

@app.route("/")
def hello_world():
    marks ={
        "john":45,
        "doe":78,
        "jane":90,
        "smith":65,
        "alice":82
        
    }
    return render_template("index.html",marks=marks)

app.run(port = 8000 ,debug=True)