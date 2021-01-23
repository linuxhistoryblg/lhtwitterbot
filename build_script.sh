#!/usr/bin/env bash

# Start dev container
container=$(buildah from fedora)

# Copy app.tgz to container
buildah copy $container app.tgz /tmp/app.tgz

# Unpack app.tgz into container /opt
buildah run $container tar xvzf /tmp/app.tgz -C /opt

# Install pip3 in container
buildah run $container dnf install -y python3-pip

# Install required python modules
buildah run $container pip3 install -r /opt/requirements.txt

# Set container working directory to /opt
buildah config --workingdir /opt $container

# Set entrypoint
buildah config --entrypoint "/usr/bin/python3 /opt/main.py" $container

# Commit container to local registry
buildah commit $container lhtwitterbot
