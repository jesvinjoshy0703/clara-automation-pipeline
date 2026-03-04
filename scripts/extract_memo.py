import json
import sys

transcript_path = sys.argv[1]
account_id = sys.argv[2]

with open(transcript_path, "r", encoding="utf-8") as f:
    text = f.read().lower()

memo = {
    "account_id": account_id,
    "company_name": None,
    "business_hours": None,
    "office_address": None,
    "services_supported": [],
    "emergency_definition": [],
    "emergency_routing_rules": None,
    "non_emergency_routing_rules": None,
    "call_transfer_rules": None,
    "integration_constraints": [],
    "after_hours_flow_summary": None,
    "office_hours_flow_summary": None,
    "questions_or_unknowns": [],
    "notes": "Extracted from demo transcript"
}

# simple keyword detection
if "sprinkler" in text:
    memo["services_supported"].append("sprinkler service")

if "fire alarm" in text:
    memo["services_supported"].append("fire alarm service")

if "emergency" in text:
    memo["emergency_definition"].append("caller mentioned emergency")

if memo["services_supported"] == []:
    memo["questions_or_unknowns"].append("services not clearly mentioned")

print(json.dumps(memo, indent=2))