---
_db_id: 67
content_type: topic
prerequisites:
  hard:
  - topics/linux/os-environmental-variables
  soft: []
ready: true
tags:
- docker-compose
- postgres
title: Intro to Docker and Docker-compose
---

[What is Docker](https://opensource.com/resources/what-docker)

Why is docker cool? Here's the first part of a three part tutorial on microservices. You don't need to read all three parts. Basically it illustrates how docker revolutionised our industry. [Here you go](https://www.codementor.io/@sheena/hello-microservice-deployment-part-1-docker-kw9ejpd9o)

## Set up

In this section we'll get docker set up on your computer. Then we'll use it to run a mysql server. This is cool because:

- you can use mysql without having to actually install mysql
- the same technique will work for running any other database (or many other applications) once docker is installed. This means you can play and experiement with different tools without much of a fuss

### Install docker

For Ubuntu:

1. https://docs.docker.com/install/linux/docker-ce/ubuntu/
2. https://docs.docker.com/install/linux/linux-postinstall/

For Mint:

1. follow these instructions https://docs.docker.com/install/linux/docker-ce/ubuntu/ then when it is time to call `add-apt-repository` rather do this:
   `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(. /etc/os-release; echo "$UBUNTU_CODENAME") stable"`
2. https://docs.docker.com/install/linux/linux-postinstall/

For Mac:

https://docs.docker.com/docker-for-mac/install/

### Super important

For some reason most people don't follow ALL the installation instructions.

Please do this:

https://docs.docker.com/engine/install/linux-postinstall/

### Now install docker-compose

https://docs.docker.com/compose/install/

### Create a docker-composition file

Make a file called `docker-compose.yaml`. This is where you specify what containers you want to run and how you want them "constructed". Paste the following into the file:

{{% code_snippet "docker-compose-pg.yaml" %}}

Now open up a terminal and `cd` into the directory containing the docker compose file then say `docker-compose up`

This launches two containers. One for postgresql, and one for adminer. Adminer is a simple web based gui that you can use to interact with different databases. You'll be able to see this UI at [http://localhost:8080](http://localhost:8080)

## Alternatively: Mysql composition

You can run a mysql composition like this one

{{% code_snippet "docker-compose-mysql.yaml" %}}

What's the difference? Postgresql is more of an industry standard than Mysql. But they are both great tools.

## Advanced topics

If you want to use Docker containers in production then there are a bunch of extra things you need to know about. Some of these concepts are pretty deep but you don't need to be an expert in order to use them.

### Volumes

If you are running a container that needs to store data (like a database) and you want to make sure that you don't lose that data if the container dies (or gets explicitly killed) then you need to use volumnes. Basically a volume is like a linux "link" or windows "shortcut". It maps a totally normal directory/folder on your computer (your computer is the host) to a directory within the container. When the container tries to store something in the directory then that data appears in the host directory.

Now if the container completely disappears the data still exists.

One use case for this behavior is upgrading. Let's say you are running `mysql:8.0`. Your compose file will initially contain something like this

```
 db:
    image: mysql:8.0
    volumes: /my/own/datadir:/var/lib/mysql
```

To upgrade, you can simply do the following:

1. kill the docker composition
2. Edit the compose file to say something like this:

```
 db:
    image: mysql:8.0.17
    volumes: /my/own/datadir:/var/lib/mysql
```

Now just `docker-compose up` and you have upgraded your mysql version. Easy peasy. And the same thing can be done for many other applications.

Another use case of volumes is of course backing up your data or movving your database to a new computer. Can you figure out how?

### ports

I'm not going to get into the definition of a port here. We'll just talk about how to configure them. Remember how we accessed the adminer gui on port 8080 a second ago? Adminer exposes port 8080 by default.

Try editing your docker compose file to contain this:

```
  adminer:
    image: adminer
    restart: always
    ports:
      - 9090:8080   ###### see how this line changed?
```

Now restart your composition.

Try out these links:

- [http://localhost:8080](http://localhost:8080)
- [http://localhost:9090](http://localhost:9090)

### Creating your own docker images

Prerequisites: It would be really useful if you were comfortable with Bash.

[https://docs.docker.com/get-started/part2/](https://docs.docker.com/get-started/part2/)