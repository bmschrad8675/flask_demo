from flask import Flask

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return """
        <h1> Welcome </h1>
        <div> You are authorized to view company information for id: 123 </div>
        <div> The sample endpoint to view users list for the company is: '/users/123'
        """


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
