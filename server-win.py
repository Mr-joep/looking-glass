from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        option = request.form['option']
        if option == 'ping':
            result = subprocess.run(['ping', ip_address], capture_output=True, text=True)
        elif option == 'tracert':
            result = subprocess.run(['tracert', ip_address], capture_output=True, text=True, shell=True)
        else:
            result = "Invalid option selected."
        return render_template('result.html', result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
