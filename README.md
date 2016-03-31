# pymailsort

pymailsort lets you sort emails using python code, especially regexes.
Primary target is the [Uberspace](https://uberspace.de/) setup.

## "Screenshot"

* Mails get sorted
* Log file looks somewhat like
```
2016-03-31T13:33:24.300985 checking new mail
2016-03-31T13:33:24.301756 sorting to ping-mails because ping@example.de matches ping@example.de in To
2016-03-31T13:33:24.301851 checking new mail
2016-03-31T13:33:24.302041 sorting to ping-mails because ping@example.de matches ping@example.de in To
2016-03-31T13:33:24.302123 checking new mail
2016-03-31T13:33:24.302456 sorting to lists.cron because <SHELL=/bin/sh> matches .{10,1000} in X-Cron-Env
2016-03-31T13:33:24.302503 checking new mail
2016-03-31T13:33:24.302745 sorting to lists.cron because <SHELL=/bin/sh> matches .{10,1000} in X-Cron-Env
```

## Setup/Testing

* copy `src/pymailsort_cfg.py.sample` to `src/pymailsort_cfg.py`
* **adjust the regexes in `src/pymailsort_cfg.py`**
* put test emails in `tests/data`
* run `bash run-tests.sh` to see if the filtering works as expected

## Installation

* change `upload.sh` to refer to your uberspace
* change `mailfilter` at `MAILADDRESS = "example@example.com"` to include your mail address
* run `bash upload.sh`

## Debugging

* in Uberspace: `tail -f pymailfilter.log`
* in Uberspace: `tail -f mailfilter.log`

## Contact

via https://github.com/mnagel/pymailsort

## License

Files:

* `*`

Copyright:

* 2014-2016 Michael Nagel ubuntu@nailor.devzero.de

License:

* The MIT License (MIT)