from flask_app import app

@app.route("/home2")
def home2():
    return 'This is Second Home.'
