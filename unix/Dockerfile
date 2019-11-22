FROM ubuntu:latest

# Install requirements
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q \
    curl telnet

# Copy configuration files
COPY localrc /root/.localrc
RUN echo 'source "/root/.localrc"' >> /root/.bashrc

# Set working directory
WORKDIR /talk

# Clean the screen and run bash
ENTRYPOINT clear && /bin/bash
