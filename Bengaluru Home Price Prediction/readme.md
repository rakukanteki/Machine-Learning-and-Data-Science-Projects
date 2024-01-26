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
