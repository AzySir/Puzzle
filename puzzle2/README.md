# Puzzle 2 - Build a Docker Image

**Scope:** Create a (linux) docker image with Web API which returns your name and email address.


To build the image

```
docker build . -t azysir/whoami 
```

To run the container
```
docker run -it -rm -p 8080:80 --name puzzle2-container azysir/whoami
```

```

Browse http://localhost:8080/api/email and see what it returns.

```json
{
    "displayName": "Adam Sir", 
    "emailAddress": "adam.sir@testproject.com"
}
```

**Dockerhub:** https://hub.docker.com/repository/docker/azysir/whoami