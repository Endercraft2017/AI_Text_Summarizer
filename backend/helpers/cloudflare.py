import subprocess
import re

def run_cloudflare_tunnel():
    # Start the cloudflared tunnel process
    process = subprocess.Popen(
        ["cloudflare", "tunnel", "--url", "http://127.0.0.1:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True,
    )

    url_pattern = re.compile(r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com")

    tunnel_url = None

    # Read output line by line
    for line in process.stdout:
        print(line, end='')  # Optional: print the output for debugging
        match = url_pattern.search(line)
        if match:
            tunnel_url = match.group(0)
            break

    if tunnel_url:
        print(f"Tunnel URL found: {tunnel_url}")
    else:
        print("Tunnel URL not found in output.")

    return tunnel_url