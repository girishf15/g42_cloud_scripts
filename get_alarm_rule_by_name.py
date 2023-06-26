import os
import requests
import json
import pandas as pd

from sign_requests.apig_sdk import signer

# load env variables
from dotenv import load_dotenv
load_dotenv()

sig = signer.Signer()
sig.Key = os.environ.get("KEY")
sig.Secret = os.environ.get("SECRET")


project_id = "xxxxxxxxxxxxxxxxxxxxx" //add your project id
alarm_id = "alxxxxxxxxxxxxxxxxxxxxx" //add your alarm_rule_id

alarm_url = f"https://ces.ae-ad-1.g42cloud.com/V1.0/{project_id}/alarms/{alarm_id}"


print(alarm_url)
headers = {"Content-Type" : "application/json; charset=UTF-8"}
r = signer.HttpRequest(method="GET", url=alarm_url, headers=headers)
sig.Sign(r)

resp = requests.request(method=r.method, url=r.scheme + "://" + r.host + r.uri, headers=r.headers)
rule_details = resp.json()

with open("single_rule.json", "w") as f:
    f.write(json.dumps(rule_details))

