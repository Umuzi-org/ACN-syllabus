# start-k3s
This is the content of start-k3s.

# 4.1.3 Start k3s

This time around we are starting the k3s cluster without trafik and using the postgres that is running locally, in production likely your postgresdb will be outisde of the cluster and maintained seperately

{% code overflow="wrap" %}
```
sudo curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable=traefik --datastore-endpoint=postgres://k3s:yourpassword@localhost:5432/kubernetes" sh -
```
{% endcode %}