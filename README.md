Gandi DNS Updater
=================
If you host a service behind your home router with a Gandi provided domain, without the ability to use a static IP, then this utility can come in handy.\
This script allows you to update your DNS record to your current public IP using Gandi's REST API.

Setup
=====
Simply fill-in `API_KEY`, `FQDN`,  `RRSET_NAME` and `RRSET_TYPE` globals, configure a crontab and you're good to go.
