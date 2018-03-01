#!/bin/bash

#I want this script to
# Accepts Argument Tag
TAG=$1

# Cleanup tmp directory
rm -Rf /tmp/ColdOnesStaging/
rm -f /tmp/ColdOnes.$TAG.tar.gz

# Clone to tmp directory
git clone . /tmp/ColdOnesStaging/

# checkout tag
cd /tmp/ColdOnesStaging/
git checkout tags/$TAG

# Zip Clone
tar -czvf /tmp/ColdOnes.$TAG.tar.gz .

# scp Clone to vultr.staging.coldones:/tmp/
scp /tmp/ColdOnes.$TAG.tar.gz vultr.staging.coldones:/tmp/

# on host:
# unpack contents into directory with name ColdOnes-$TAG
ssh -t root@vultr.staging.coldones "mkdir ~/ColdOnes-$TAG && tar -xvzf /tmp/ColdOnes.$TAG.tar.gz -C ~/ColdOnes-$TAG"
