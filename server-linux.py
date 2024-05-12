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
            result = subprocess.Popen(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, _ = result.communicate()
        elif option == 'tracert':
            result = subprocess.Popen(['traceroute', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, _ = result.communicate()
        else:
            result = "Invalid option selected."
            output = ""
        return render_template('result.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)
