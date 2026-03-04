import os
import json
import subprocess

demo_folder = "dataset/demo_calls"
output_folder = "outputs/accounts"

files = os.listdir(demo_folder)

account_number = 1

for file in files:
    if file.endswith(".txt"):
        transcript = os.path.join(demo_folder, file)
        account_id = f"account_{account_number:03d}"

        account_path = os.path.join(output_folder, account_id, "v1")
        os.makedirs(account_path, exist_ok=True)

        memo_path = os.path.join(account_path, "memo.json")
        agent_path = os.path.join(account_path, "agent_spec.json")

        # run extraction script
        memo_output = subprocess.check_output(
            ["python", "scripts/extract_memo.py", transcript, account_id]
        )

        memo_json = json.loads(memo_output)

        with open(memo_path, "w") as f:
            json.dump(memo_json, f, indent=2)

        # generate agent
        agent_output = subprocess.check_output(
            ["python", "scripts/generate_agent.py", memo_path]
        )

        agent_json = json.loads(agent_output)

        with open(agent_path, "w") as f:
            json.dump(agent_json, f, indent=2)

        print(f"Processed {account_id}")

        account_number += 1