1. `build:` Specifies the build context and Dockerfile to build the image for the service.
1. `container_name:` Specifies the name of the container for the service.
1. `command:` Specifies the command to run when the container starts.
1. `entrypoint:` Specifies the entrypoint command for the container.
1. `environment:` Specifies the environment variables to set for the service.
1. `expose:` Specifies the ports that the service should listen on, but does not publish them.
1. `image:` Specifies the image to use for the service.
1. `ports:` Specifies the ports to publish from the container to the host.
1. `volumes:` Specifies the volumes to mount from the host into the container.
1. `depends_on:` Specifies the services that the service depends on and should be started first.
1. `networks:` Specifies the networks the service should be connected to.
1. `restart:` Specifies the conditions under which the service should be automatically restarted.
1. `stdin_open:` Specifies whether the service should open its standard input stream.
1. `tty:` Specifies whether the service should allocate a TTY.
1. `healthcheck:` Specifies a command to run inside the container to check the health of the service.