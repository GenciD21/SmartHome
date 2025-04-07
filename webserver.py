from flask import Flask
from flask import request
from flask import render_template
from sql_write import db_write
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('slider.html')
    if request.method == "POST":
        CODE = request.form.get("code")
        BRIGHTNESS = request.form.get("brightness")
        DISTANCE = request.form.get("distance")
        ON = request.form.get("On")
        print(f" {CODE} {BRIGHTNESS} {DISTANCE} {ON}")
        db_write(CODE, BRIGHTNESS, DISTANCE, ON)
        return render_template('slider.html')
    

if __name__ == "__main__":
    app.run()