def getHomeMessage():
    return """
        <h1> Welcome </h1>
        <div> You are authorized to view company information for id: 123 </div>
        <div> The sample endpoint to view users list for the company is: <code>http://localhost:5050/users/123</code></div>
        <div> Updates can be made to users first name buy a PUT request to <code>http://localhost:5050/users/6?firstName=John</code></div>
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
