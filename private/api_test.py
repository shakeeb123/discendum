# -*- coding: utf-8 -*-

import json
import requests
url = "http://127.0.0.1:8000/discendum"

data = {
    "email": [
        "foo@example.com",
        "baz@example.com",
        "zuul@example.com",
        "ziff@example.com",
        "unknown@example.com"
    ]
}

print "Checking for email addresses"
r = requests.post("{!s}/email_api/check_email.json".format(url), data = json.dumps(data))
print (r.json())
