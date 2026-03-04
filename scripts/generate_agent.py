import json
import sys

memo_file = sys.argv[1]

with open(memo_file) as f:
    memo = json.load(f)

agent = {
    "agent_name": f"{memo.get('company_name','Client')} Clara Agent",
    "voice_style": "professional friendly",
    "variables": {
        "timezone": None,
        "business_hours": memo["business_hours"],
        "address": memo["office_address"]
    },
    "system_prompt": "You are Clara, an AI receptionist handling inbound calls.",
    "call_transfer_protocol": {
        "timeout_seconds": 60,
        "retry": 1,
        "failure_message": "Sorry, I couldn't connect the technician. They will call you shortly."
    },
    "fallback_protocol": "Collect caller details and assure callback.",
    "version": "v1"
}

print(json.dumps(agent, indent=2))