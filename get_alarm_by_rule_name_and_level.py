import os
import json
import requests

from sign_requests.apig_sdk import signer

# load env variables
from dotenv import load_dotenv
load_dotenv()

sig = signer.Signer()
sig.Key = os.environ.get("KEY")
sig.Secret = os.environ.get("SECRET")


project_id = "0xxxxxxxxxxxxxxxxxxxxxxx"
rule_name = "all-disk-alert-xxxxxxxxxxxxxxxx"
alarm_level = 2 // 1-4, 1 for critical to 4

alarm_url = f"https://ces.ae-ad-1.g42cloud.com/V1.0/{project_id}/alarm-histories?alarm_name={rule_name}&alarm_level={level}"

headers = {"Content-Type" : "application/json; charset=UTF-8"}
r = signer.HttpRequest(method="GET", url=alarm_url, headers=headers)
sig.Sign(r)

print(r.headers)
resp = requests.request(method=r.method, url=r.scheme + "://" + r.host + r.uri, headers=r.headers)
all_alarm_details = resp.json()

with open("alarms.json", "w") as f:
    f.write(json.dumps(all_alarm_details))
