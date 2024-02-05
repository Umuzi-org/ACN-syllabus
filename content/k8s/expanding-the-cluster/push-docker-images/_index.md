# 3.2.5 Push docker images to harbor

First, let's install Docker on this instance. Refer to the 2.2.1 chapter for the instructions.

In your browser navigate to `https://harbor.<your-domain>` and login using the username `admin` and password you created in the `values.yaml` file.

Go to projects and create a project called `application`.

Now go to your command line and let's issue some Docker commands to login into Harbor, build the Nginx image and push it to Harbor. Remember to substitute `<your-domain>` with the domain given to you by Umuzi.

```
# logs in into Harbor
docker login harbor.<your-domain>

# builds the Nginx image
cd /home/ubuntu/umuzi-k8s/nginx
docker build . -t harbor.<your-domain>/application/nginx:v1

# pushes the image to Harbor
docker push harbor.<your-domain>/application/nginx:v1
```

Let's do the same from the Python app using a oneliner:

```
cd /home/ubuntu/umuzi-k8s/python
docker build . -t harbor.<your-domain>/application/python:v1 --push
```



