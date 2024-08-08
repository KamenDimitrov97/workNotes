# Adding labels to your docker images

## Setting Labels in Dockerfile

Labels in Dockerfiles provide a way to embed metadata directly into your Docker images. You can add labels using the LABEL instruction in your Dockerfile. Here’s an example:

```Dockerfile
# Use an official base image
FROM ubuntu:latest

# Add labels
LABEL repository=flaxandteal
LABEL maintainer="kamen@flaxandteal.co.uk"
LABEL version="1.0"

# Your Dockerfile instructions
RUN apt-get update && apt-get install -y 

CMD ["bash"]
```

## Setting Labels When Creating Images

You can also set labels during the image build process using the docker build command. Here’s how you can specify labels:

```sh
docker build --label repository=flaxandteal --label maintainer="kamen@flaxandteal.co.uk" --label version="1.0" -t my-image:latest .
```

# Checking your image labels

To inspect the labels of an existing image:

```sh
docker inspect --format='{{json .Config.Labels}}' my-labeled-image:latest
```

# Using image labels

## Listing images using a label

Labels can help you organize and filter images.

```sh
docker image ls --filter "label=repository=flaxandteal"
docker image ls --filter "label=maintainer=kamen@flaxandteal.co.uk"
docker image ls --filter "label=version=1.0"
```

## Deleting Images Based on Labels

You can remove all images that appeal to a certain label.

```sh
docker image prune --filter "label=label_name(repository)=flaxandteal"
docker image prune --filter "label=version=1.0"
docker image prune --filter "label=maintainer=kamen@flaxandteal.co.uk"
```

## Interesting ways to use labels

### Metadata and Documentation

1. Keeping your images versioned.
2. Small description that you can use when inspecting your images.
3. Different filtering option to search images by

```Dockerfile
LABEL version="1.0"
LABEL description="This is a web server image based on Ubuntu."
LABEL maintainer="your-email@example.com"
LABEL license="MIT"
```

### Build information 

You can log build information.
```Dockerfile
LABEL build_date="2024-05-21"
LABEL build_tool="Docker 20.10.7"
LABEL git_commit="abc123"
LABEL git_repository="https://github.com/user/repo"
```

### Environment information
Cluster information, which image to be used where. 
```Dockerfile
LABEL env="production"
LABEL region="us-west"
```

### You can integrate dynamic labels into CI/CD processes to setup up your images for different environment

```Dockerfile
LABEL ci_pipeline="jenkins"
LABEL ci_status="passed"
```

### Security

```Dockerfile 
LABEL vulnerability_scanned="true"
LABEL compliance="HIPAA"
LABEL security_patch_level="2024-05-01"
```

### Usage and resource information

```Dockerfile
LABEL usage="high-memory"
LABEL memory_limit="4GB"
LABEL cpu_limit="2"
```

### Much more