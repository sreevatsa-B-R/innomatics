from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Results page for regex matching
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error as e:
        matches = [f"Error in regex: {e}"]
    
    return render_template('index.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)

# Route to validate email
@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        # Simple email regex pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_pattern, email):
            result = "Valid Email"
        else:
            result = "Invalid Email"
        return render_template('validate_email.html', email=email, result=result)
    return render_template('validate_email.html')

if __name__ == '__main__':
    app.run(debug=True)
