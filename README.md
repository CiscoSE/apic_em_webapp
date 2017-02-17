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
- ciscosparkapi (0.4.2)

Installing
----------

Once you clone the repository, you will notice a "manage.py" in the apic_em_webapp directory.  If django is properly installed, you should be able to launch a simple webserver and test the app.

- "python manage.py runserver"
- browse to "http://127.0.0.1:8000/apic"
    - if all is installed properly, you should see the running configuration of a virtual router in the Cisco APIC-EM sandbox
- browse to "http://127.0.0.1:8000/apic/api/v1"
    - you should see a JSON representation of the same configuration
- Spark configuration
    - This application presumes it will be accessible from the Internet.  If you will be on a private network or behind a firewall you do not manage, please see the ciscosparkapi examples for code on how to use ngrok.  https://github.com/CiscoDevNet/ciscosparkapi
    - Create a file called "at.txt" in the apic_em subdirectory.  Paste an authentication token from developer.ciscospark.com for your bot into the at.txt file.
    - Open the apic_em/bot.py and edit the "web_server" argument with the publicly accessible IP or URL for you server.
    - Browse to http://127.0.0.1:8000/apic/wh_init to initialize the webhook.

Authors
-------

Brian Buxton - index and apic_em

Chris Lunsford - ciscosparkapi examples - Much of the Spark classes and functions I wrote are highly derivative of Chris' examples

django tutorials - polls directory include work through lesson 4

License
-------

This project is published under the GPL 3.0 license.

Change Log
----------

2/7/17 - added /api/v1/ as a demonstration of serialized JSON output of the config.

2/9/17 - added /wh_init/ adapting ciscosparkapi example code to django

2/10/17 - added /sparkwebhook/ adapting ciscosparkapi example to django.  Also resolved circular import statements in views, get_stuff and bot.