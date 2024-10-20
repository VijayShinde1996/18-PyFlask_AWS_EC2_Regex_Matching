from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  matches = []
  return render_template('index.html', matches=matches)

@app.route('/results', methods=['POST'])
def results():
  test_string = request.form['test_string']
  regex = request.form['regex']
  matches = []
  try:
    matches = re.findall(regex, test_string)
  except re.error as e:
    matches = [f"Error: {str(e)}"]
  return render_template('index.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
  email = request.form['email']
  email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
  if re.match(email_regex, email):
    return "Valid Email!"
  else:
    return "Invalid Email!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)