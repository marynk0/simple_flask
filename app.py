from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__== "_main_":
    app.run(debug=True)