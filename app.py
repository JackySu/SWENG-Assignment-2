from flask import Flask, render_template, request
import calc


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        ex = request.form['expr']
        return render_template('index.html', RESULT=str(calc.main(s=ex)))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
