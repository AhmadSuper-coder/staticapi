import os

def set_static_ip():
    interfaces_file_path = '/etc/network/interfaces'
    networking_file_path = '/etc/default/networking'

    configure_interfaces = input("Is CONFIGURE_INTERFACES set to 'no'? (yes/no): ")
    if configure_interfaces.lower() != 'no':
        os.system("sudo sh -c 'echo \"CONFIGURE_INTERFACES=no\" >> /etc/default/networking'")

    ip_address = input("Enter the static IP address: ")
    netmask = input("Enter the netmask: ")
    gateway = input("Enter the gateway address: ")
    dns_servers = input("Enter DNS nameservers separated by spaces (e.g., 103.8.45.5 103.8.45.6): ")

    # Write network interfaces configuration to the file
    with open(interfaces_file_path, 'w') as interfaces_file:
        interfaces_file.write(f"auto wlp1s0\n")
        interfaces_file.write(f"iface eth0 inet static\n")
        interfaces_file.write(f"address {ip_address}\n")
        interfaces_file.write(f"netmask {netmask}\n")
        interfaces_file.write(f"gateway {gateway}\n")
        for dns in dns_servers.split():
            interfaces_file.write(f"dns-nameservers {dns}\n")

if __name__ == "__main__":
    set_static_ip()


# Enter the static IP address: 192.168.1.117
# Enter the netmask: 255.255.255.0
# Enter the gateway address: 192.168.1.1
# Enter DNS nameservers separated by spaces (e.g., 103.8.45.5 103.8.45.6): 192.168.1.1 8.8.8.8
