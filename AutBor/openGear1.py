from netmiko import ConnectHandler

opengear = {
    "device_type": "opengear",
    "host": "192.168.0.1",
    "username": "root",
    "password": "KC'TfG=Fi.TtF%Qs",
    "fast_cli": False, #opengear shells can be slow to respond

}

connection = ConnectHandler(**opengear)
prompt = connection.find_prompt()
print("Prompt Detected:", prompt)

output = connection.send_command_timing("uptime")
print("\nUptime:\n", output)

print(connection.send_command_timing("hostname"))

status = connection.send_command_timing("ogcli status")
print(status)
if "online" in status:
    print("OpenGear reports healthy status.")
connection.disconnect()

""" def get_opengear_info():
    connection = ConnectHandler(**opengear)
    print("Connected to Opengear\n")

    output = connection.send_command("uptime")
    print("Uptime: \n", output, "\n")

    connection.disconnect()

    if __name__ == "__main__":
        get_opengear_info() """