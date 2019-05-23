from flask import Flask, render_template, request, redirect, url_for
import json, requests

app = Flask(__name__)


def fixer(convert_to, base = 'EUR'):
    API_KEY = '010a04660436d98ab0fdbc8021536d25'
    url = f'http://data.fixer.io/api/latest? \
        access_key={API_KEY}& \
        base=EUR& \
        symbols={convert_to}& \
        format=1' 

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return parsed


@app.route('/', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':

        parsed = fixer(request.form.get('convert_to'), request.form.get('base'))
        
        return render_template('form.j2', parsed = parsed, to = request.form.get('convert_to'), amount = float(request.form.get('amount')))
    return render_template('form.j2', parsed = '')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80) # tiangolo defult for docker
    #app.run(debug=True)     # for local

