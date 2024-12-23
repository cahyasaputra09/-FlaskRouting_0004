from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'asu {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Mengambil data dari form POST
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')  # Mengambil data dari query string GET
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
