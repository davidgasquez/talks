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
ENV TERM xterm-256color

# Install Python packages
RUN pip3 install -U pip
RUN pip install click wikipedia spacy pygments

RUN python3 -m spacy download en_core_web_sm

# Add local user
RUN adduser --disabled-password --gecos '' local

# Copy configuration files
COPY localrc /home/local/.localrc
RUN echo 'source "/home/local/.localrc"' >> /home/local/.bashrc

USER local

COPY clis/ /talk/clis
COPY scripts/ /talk/scripts

# Set working directory
WORKDIR /talk

# Clean the screen and run bash
ENTRYPOINT clear && /bin/bash
