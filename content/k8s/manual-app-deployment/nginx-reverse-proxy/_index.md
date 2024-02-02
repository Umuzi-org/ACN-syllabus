---
title: Nginx Reverse Proxy
content_type: project
tags:
- kubernetes
- nginx
prerequisites:
  hard:
  - k8s/manual-app-deployment/nginx-tls
  - k8s/manual-app-deployment/python-app-setup
  soft: []
ready: true
submission_type: link
---

We will now connect the Nginx and the Python application by configuring Nginx as a reverse proxy, pointing the `/api` route to the Python app local address. With that, we will be able to access the Python app externally at `https://your-domain/api`.

First, add the following block in the `nginx.conf` file, under the `server` HTTPS block.

```nginx
location /api {
    # local Python app address
    proxy_pass http://127.0.0.1:5000;
}
```

Also, replace the `nginx/index.html` file with the following content. It will add a nice frontend our application.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to This Nginx Page</title>
    <style>
        #status-light {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: red;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome, press the button right now</h1>
    <p>This is a simple landing page hosted by Nginx on your server.</p>
    <button id="get-status-button">Press my button</button>
    <p>Button Press Count: <span id="count">0</span></p> <!-- Added this line -->
    <div id="status-light"></div>
    
    <script>
        // JavaScript code to handle the button click and status update
        document.getElementById('get-status-button').addEventListener('click', () => {
            // Send a request to increment the value
            fetch('/api/pressed', { method: 'GET' }) // Sending a GET request to the /pressed route
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    }
                    throw new Error('Request failed.');
                })
                .then(data => {
                    // Update the count display
                    document.getElementById('count').textContent = data.count;
                    // Log the response for debugging
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    </script>
</body>
</html> 
```

On your EC2 instance, pull the changes, copy the files and restart Nginx:

```
# pull the changes
cd /home/ubuntu/umuzi-k8s
git pull

# copy files
sudo cp nginx/nginx.conf /etc/nginx/conf.d/nginx.c
sudo cp nginx/index.html /var/www/html/

# restart nginx
sudo systemctl restart nginx
```

Now you should be able to access the Python app externally! Try it on your browser with the `https://your-domain` address.