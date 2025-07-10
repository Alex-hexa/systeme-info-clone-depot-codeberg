
# Commandes de base

Lister tous les containers actifs

```bash
docker ps
```

Lister tous les containers

```bash
docker ps -a
```

Lister toutes les images

```bash
docker images
```

Lister tous les sous-réseaux

```bash
docker network ls
```

Consulter le log d'un container existant

```bash
docker logs $container_name
```

# Container PostgreSQL

## Démarrage de container

### Version courte

```bash
docker run --name tpdocker -e POSTGRES_DB=tpdocker -e POSTGRES_PASSWORD=toto -d postgres
```


### Version longue

```bash
docker pull postgres
docker create --name tpdocker -e POSTGRES_DB=tpdocker  -e POSTGRES_PASSWORD=toto postgres
docker start tpdocker
```

## Connexion à l'instance depuis le container

### Version spécifier l'utilisateur pour exec

```bash
docker exec -it -u postgres tpdocker psql tpdocker
```

### Version spécifier l'utilisateur pour psql

```bash
docker exec -it tpdocker psql -U postgres tpdocker
```