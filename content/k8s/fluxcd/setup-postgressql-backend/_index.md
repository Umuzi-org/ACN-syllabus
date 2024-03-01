# setup-postgressql-backend
This is the content of setup-postgressql-backend.

# 4.1.2 Setup postgressql backend

When no flags are used when starting k3s it uses a sqlite backend that's not very stable and quickly fails. To give us a more sturdy backend let's use postgressql instead.

```
# logs in as the `postgres` user
sudo -i -u postgres

# opens the PostgreSQL shell
psql

# creates the databse
CREATE DATABASE kubernetes;

# creates the user/password
CREATE USER k3s WITH PASSWORD 'yourpassword';

# allows the user access to the databse
GRANT ALL PRIVILEGES ON DATABASE kubernetes TO k3s;

# exits the PostgreSQL shell
exit

# logs back to your instance user
logout
```