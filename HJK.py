from flask import Flask , redirect, url_for, request, render_template, jsonify
app = Flask(__name__)
import cal_algorithm
@app.route('/')
def hello_world():
    return render_template("calculater.html")

@app.route('/answer', methods = ["POST"])
def asd():
    text = request.form['textview']
    return_answer = cal_algorithm.cal_algorithm(text)
    return render_template("answer.html", answer = return_answer)

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)


