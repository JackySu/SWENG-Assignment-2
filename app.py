from flask import Flask, render_template, request
import calc


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        s = request.form['expr']
        try:
            res = calc.main(s=s)
            if res is not None:
                res = f'{res:.3f}'
                return render_template('index.html', RESULT=res)
        except Exception as exc:
            print(exc)
            return render_template('index.html', ERROR=exc)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
