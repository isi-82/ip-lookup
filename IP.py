import socket
from discordwebhook import Discord

hook = Discord(url="<webhook_url>")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"{hostname} IP Addr:{local_ip}")
hook.post(
    embeds=[{"title": hostname, "description": f"IP Addr: {local_ip}"}],
    username="Webhook Name"
)