# apic_em_webapp

This is a project where I will explore network programmability and other programming concepts with python.

Getting Started
---------------

These instructions should get the apps running for you in a developer environment.  These apps were not written to be deployed in production and currently lack any authentication or RBAC.

Pre-requisites
--------------

You will need the following python modules for many of the apps to run.:
- django (1.10.5)
- django-filter (1.0.1)
- djangorestframework (3.5.3)
- requests (2.13.0)

Installing
----------

Once you clone the repository, you will notice a "manage.py" in the apic_em_webapp directory.  If django is properly installed, you should be able to launch a simple webserver and test the app.

- "python manage.py runserver"
- browse to "http://127.0.0.1:8000/apic"
- if all is installed properly, you should see the running configuration of a virtual router in the Cisco APIC-EM sandbox

Authors
-------

Brian Buxton - index and apic_em
django tutorials - polls

License
-------

This project is published under the GPL 3.0 license.

Change Log
----------

2/7/17 - added /api/v1/ as a demonstration of serialized JSON output of the config.