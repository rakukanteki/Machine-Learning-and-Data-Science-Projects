# Flask:
Flask is a web framework written in Python. It is designed to build websites easily and more effectively.
It provied essential components for web development, routing, requests made by the user and response.
- Routing:
  1. Flask uses decorators to define routes. A route is a URL associated with a Python function.
  2. Flask handles HTTP requests and responses.
  3. Flask includes templating engine (Jinja2) which allows developers to create HTML templates.
  4. We can also add third party extensions to add Database integration, authentications and more.

# Using:
1. We can create an instance of the Flask class like below, 
  ```
  from flask import Flask, request, jsonify
  object_name = Flask(__name__)
  ```
2. We can create a route and define the functionalities of that route. Like,
  ```
  @app.route('/function_name')
  def function_name():
    statements....
    ..............
  ```
3. When a Python script is executed, Python sets a special built-in variable called __name__ for the script being run. If the script is the main program being executed, __name__ is set to "__main__". Like,
  ```
  if __name__ == "__main__":
    statements..
    app.run()
    # app.run() is a method that starts the development server,
    # allowing you to run and test 
    # your Flask application
  ```
