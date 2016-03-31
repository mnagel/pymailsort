#! /bin/bash
HOST="my-uberspace-host.com"
scp src/pymailsort.py $HOST:bin/pymailsort.py
scp mailfilter $HOST:.mailfilter
