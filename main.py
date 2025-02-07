# import logging
# import subprocess
# import pathlib
# import uvicorn


# def ip_addy():
#     ip = (
#         subprocess.check_output("ipconfig")
#         .decode("utf-8")
#         .split("IPv4 Address. . . . . . . . . . . : ")[2]
#         .split("Subnet Mask")[0]
#     )
#     return f"\nserver runniyng on : https://{ip.strip()}:443\n"


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     ssl_keyfile_path = pathlib.Path("localhost+2-key.pem")
#     ssl_certfile_path = pathlib.Path("localhost+2.pem")
#     uvicorn.run(
#         "nuclei_backend:app",
#         host="0.0.0.0",
#         port=80,
#         workers=4,
#         reload=True,
#         use_colors=True,
#         ssl_keyfile=ssl_keyfile_path,
#         ssl_certfile=ssl_certfile_path,
#     )

import redis

# Create a Redis client instance
r = redis.Redis(
    socket_timeout=5,
).from_url("rediss://gleaming-fowl-nbdqvk.ziska44n.traefikhub.io:6379/0")

# Set a value in Redis
r.set("mykey", "myvalue")

# Get a value from Redis
value = r.get("mykey")
print(value)
