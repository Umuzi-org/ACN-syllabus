# helmrelease-harbor
This is the content of helmrelease-harbor.

# 4.1.10 Helmrelease harbor

You know the drill by now&#x20;

```
|-- infrastructure
|   |-- harbor
|   |   |-- kustomization.yaml
|   |   |-- kustomizeconfig.yaml
|   |   |-- release.yaml
|   |   |-- values.yaml
|   |   |-- namespace.yaml
|   |   |-- issuer.yaml
```

You can create the release yourself here are some commands that may help you

```
kubectl -n flux-system get kustomization
kubectl -n flux-system get helmchart
kubectl get ns
kuebctl -n harbor get helmrelease
```
