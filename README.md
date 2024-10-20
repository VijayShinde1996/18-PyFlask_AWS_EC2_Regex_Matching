Markdown
# Regex Matcher App

This is a web application built with Flask that allows users to input a test string and a regular expression (regex) and displays all the matches found. It also includes email validation functionality.

**Features:**

- Find matches for regular expressions in text strings.
- Validate email addresses using a regular expression.
- User-friendly interface with forms for input and clear display of results.

**Getting Started:**

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your_username/regex-matcher-app.git](https://github.com/your_username/regex-matcher-app.git)
Use code with caution.

Install dependencies:

Bash
pip install Flask
Use code with caution.

Run the application:

Bash
python app.py
Use code with caution.

Open your web browser:

Navigate to http://localhost:5000 to access the application.

Usage:

Enter your test string in the "Test String" field.

Enter your desired regular expression in the "Regular Expression" field.

Click the "Find Matches" button.

The application will display all the matches found within the test string, or an error message if the regex is invalid.

To validate an email address:

Enter the email address in the "Email" field.
Click the "Validate Email" button.
The application will display "Valid Email!" or "Invalid Email!" based on the validation result.
Technologies:

Python
Flask web framework
Regular expressions (re module)
