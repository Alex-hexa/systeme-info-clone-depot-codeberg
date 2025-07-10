# TP Stateless

![](./tp-stateless.drawio.png)

Pour tester l'accès au service proxifiée :

```
http://localhost:8001/api/v1/namespaces/default/services/frontend/proxy/
```

# TP Statefulsets

![](./tp-stateless.drawio.png)

## Commands

```bash
kubectl scale deploy wordpress-mysql --replicas=0
kubectl get pods -l app=wordpress
kubectl scale deploy wordpress-mysql --replicas=1
kubectl get pods -l app=wordpress
kubectl scale deploy wordpress --replicas=0
kubectl get pods -l app=wordpress
kubectl scale deploy wordpress --replicas=1
```