from flask import Flask, request
import json
from misc.db_utils import db_connect, populate_users
from misc.html_utils import getHomeMessage, getTableHeader

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return getHomeMessage()


@app.route('/users/<company_id>/')
def userList(company_id):
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


@app.route('/users/<userId>', methods=['PUT'])
def addUser(userId):
    print(request.args)
    firstName = request.args.get('firstName')

    con = db_connect()
    cur = con.cursor()
    user_sql = f"UPDATE users SET first_name = '{firstName}' where id = {userId}"
    print(user_sql)

    cur.executescript(user_sql)

    return f'User id: {userId} updated with first name: {firstName}'


@app.route('/users/generate/')
def generateUsers():
    # Create users table and populate it from csv
    populate_users()
    return 'Users table populated'


# Flask app setup
if __name__ == '__main__':
    app.run(debug=True, port=5050)
