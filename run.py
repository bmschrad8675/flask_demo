from flask import Flask
import json
from misc.db_utils import db_connect, populate_users

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return """
        <h1> Welcome </h1>
        <div> You are authorized to view company information for id: 123 </div>
        <div> The sample endpoint to view users list for the company is: '/users/123'
        """


def getTableHeader():
    header = """
                <th>id</th>
                <th>username</th>
                <th>first_name</th>
                <th>last_name</th>
                <th>email</th>
                <th>company_id</th>
            """
    return header


@app.route('/users/<company_id>/')
def userList(company_id):
    # Make sure they are authorized
    if company_id != '123':
        return f"Not authorized for Company: {company_id}"
    else:
        # User is authorized show list of their users
        con = db_connect()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE company_id = {company_id}")
        users = cur.fetchall()

        # Format user results into an html table
        txtHeader = f'<table>{getTableHeader()}'
        txtUser = ''
        for user in users:
            txtUser = txtUser + '<tr>'
            txtUser = txtUser + ''.join(map(lambda x: (f'<td>{x}</td>'), user))
            txtUser = txtUser + '</tr>'

        txtFooter = '</table>'
        
        return ''.join([txtHeader, txtUser, txtFooter])


@app.route('/users/generate/')
def generateUsers():
    # Create users table and populate it from csv
    populate_users()
    return 'Users table populated'


# Flask app setup
if __name__ == '__main__':
    app.run(debug=True, port=5050)
