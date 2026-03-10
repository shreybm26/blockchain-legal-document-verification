import subprocess
import json

def upload_to_ipfs(file_path):

    result = subprocess.run(
        ["ipfs", "add", "-Q", file_path],
        capture_output=True,
        text=True
    )

    cid = result.stdout.strip()

    return cid