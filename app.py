from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')  # '.' matlab current folder (EmptyCup)

@app.route("/listings")
def get_listings():
    return send_from_directory('static', 'listings.json')

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")  # static HTML serve karna

# @app.route("/listings")
# def get_listings():
#     return send_from_directory('static', 'listings.json')  # JSON data serve karna

# if __name__ == "__main__":
#     app.run(debug=True)
