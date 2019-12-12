FROM ubuntu:latest

# Install requirements
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q \
    curl telnet figlet toilet \
    python3 python3-pip python3-dev python3-setuptools \
    gawk jq nano

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Install Python packages
RUN pip3 install -U pip
RUN pip install click wikipedia spacy pygments

RUN python3 -m spacy download en_core_web_sm

# Add local user
RUN adduser --disabled-password --gecos '' david

# Copy configuration files
COPY localrc /home/david/.localrc
RUN echo 'source "/home/david/.localrc"' >> /home/david/.bashrc

USER david

# Set working directory
WORKDIR /talk

# Clean the screen and run bash
ENTRYPOINT clear && /bin/bash
