# Issues 

## Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Issue is using docker in docker where the inner docker must use the outer docker daemon and DOCKER_HOST must be set to that docker daemon 
but I can't seem to find what that host is..

You have probably already run containers from the Docker Hub and noticed that some of them need to bind mount the /var/run/docker.sock file. What is this file, and why it is sometimes used by containers? Short answer: it’s the Unix socket the Docker daemon listens on by default, and it can be used to communicate with the daemon from within a container.