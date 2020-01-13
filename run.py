from flask import Flask

app = Flask(__name__)

# Routes
@app.route('/users/<company_id>/')
def userList(company_id):
    # Make sure they are authorized
    if company_id != '123':
        return f"Not authorized for Company: {company_id}"
    else:
        return f"Welcome"


# Flask app setup
if __name__ == '__main__':
    app.run(debug=True)
