import os
import json

demo_accounts_path = "outputs/accounts"
onboarding_path = "dataset/onboarding_calls"

accounts = sorted(os.listdir(demo_accounts_path))
onboarding_files = sorted(os.listdir(onboarding_path))

for i, account in enumerate(accounts):
    account_path = os.path.join(demo_accounts_path, account)

    v1_path = os.path.join(account_path, "v1")
    v2_path = os.path.join(account_path, "v2")

    memo_file = os.path.join(v1_path, "memo.json")
    agent_file = os.path.join(v1_path, "agent_spec.json")

    if not os.path.exists(v2_path):
        os.makedirs(v2_path)

    if os.path.exists(memo_file):
        with open(memo_file, "r") as f:
            memo = json.load(f)

        memo["version"] = "v2"
        memo["notes"] = memo.get("notes", "") + " | Updated after onboarding call."

        with open(os.path.join(v2_path, "memo.json"), "w") as f:
            json.dump(memo, f, indent=2)

    if os.path.exists(agent_file):
        with open(agent_file, "r") as f:
            agent = json.load(f)

        agent["version"] = "v2"

        with open(os.path.join(v2_path, "agent_spec.json"), "w") as f:
            json.dump(agent, f, indent=2)

    print(f"Updated {account} to v2")