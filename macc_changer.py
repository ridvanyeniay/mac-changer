import subprocess
import optparse
import re

def user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()


def change_mac(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])


def control(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

(deneme,yanilma) = user_inputs()
change_mac(deneme.interface,deneme.mac_address)
final_mac = control(str(deneme.interface))

if final_mac == deneme.interface:
    print("basarili")
else:
    print("error")
print("MyMacChanger Started!")