# Language used:
1. HTML 5.
2. CSS.
3. JavaScript.
4. Python Programming Language.
   
# For server:
1. Python Flask.
2. Nginx web server.
   - NGINX is a light web server which can serve to HTTP requests.
     When we load the web browser, it goes to the EC2 instance where
     from NGINX web server it will return our app.html, app.css, app.js.

# Keywords:
1. Flask.
2. jsonify
   - jsonify is a function that converts a Python dictionary into a JSON response object.
     Here, we have a json file named 'columns.json'. 'columns.json' is stored as a dictionary
     file. To use that as json object, we use jsonify. Like below,
     ```
     response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
       })
     ```
     we are calling 'get_estimate_price' function from our 'util.py' module. And taking       
     parameters.
     
     {'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)}: This       
     constructs a Python dictionary with a single key-value pair. The key is 'estimated_price', 
     and the value is the result of calling the get_estimated_price function with the provided 
     arguments.

     jsonify({...}): This function takes the dictionary created in the previous step and 
     converts it into a JSON response object. The resulting JSON object will have the same 
     structure as the dictionary but will be formatted as a JSON string.

     response = jsonify({...}): This assigns the JSON response object created by jsonify to a 
     variable named response, which can then be returned from a Flask route or used in any 
     other context where a JSON response is needed.

# Working of Python Flask Server:
- Flask is a module that allows us to write Python services. It takes HTTP requests and gives     us the desired results. Flask is a web framework written in Python.
    [ N.B: We must run the flask server before opening the website. ]
  
1. Create an instance of Python Flask.
   ```
   app = Flask(__name__)
   ```

2. Here is a simple example of a functions.
   ```
   def hello():
      return "Hi"
   ```

3. Now we need to route that function to the server. For that,
   ```
   @app.route('/hello')   // Name must be same as the function name.
   def hello():
      return "Hi"
   ```

5. Here, our main function, where we will call our defined functions. 
   ```
   if __name__ = "__main__":
      print("Python Flask server is running...")
      app.run()  // calling app.run() initiates the server.
   ```
3. Finally, we go to our python terminal or cmd, go the specific folder. Then type:
   ```
   cd Server   // Going into the folder where our server.py is.
   python server.py  // Running the server.
   ```

# Technical architecture:
- When we click on a button in our website. For example, 'predict price' then app.js file will make a call to the NGINX. We will use reverse proxy setup in NGINX to route all our requests to Python Flask  Server, and it will predict the price from saved and trained ML model.

- Here,
root is the path from which the website is to be renderes. Location of my prediction website is set as root, from which the html files will be rendered.
```
location / {
            root   "C:\Users\radwa\OneDrive\Desktop\Py\Home Price Website\Interface";
            index  index.html index.htm app.html;
        }
```
