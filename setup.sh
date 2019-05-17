#!/usr/bin/env bash

## Update our operating system's (i.e. Ubuntu) package manager
sudo apt-get -y update


## Install our aplication's dependencies
sudo apt-get -y install python3-pip \
                        postgresql \
                        postgresql-contrib \
                        postgresql-server-dev-all

# for later:
# sudo -H pip3 install virtual

sudo -H pip3 install psycopg2


##







