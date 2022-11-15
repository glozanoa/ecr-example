from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def hello():
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():    
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")                           
                print(f"  Netmask: {address.netmask}")                                         
                print(f"  Broadcast IP: {address.broadcast}")
                                                      
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")                                          
                print(f"  Broadcast MAC: {address.broadcast}")
    return if_addrs

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001)
