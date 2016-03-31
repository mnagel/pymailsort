#! /bin/bash
HOST="my-uberspace-host.com"
scp src/pymailsort.py $HOST:bin/pymailsort.py
scp src/pymailsort_cfg.py $HOST:bin/pymailsort_cfg.py
scp mailfilter $HOST:.mailfilter
