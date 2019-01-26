#!/usr/bin/env python


import subprocess

import optparse

import re

def get_arguments():
    # parser pour passer des arguments kima n7abo f cmd
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="L'interface li nbdlolo mac adresse")
    parser.add_option("-m", "--mac", dest="newmac", help="La nouvelle mac adresse kho")
    (options, arguments) = parser.parse_args() #we can use [0] at the end and just use options =
    if not options.interface:
        parser.error("Nsit tmed ama interface kho dir --help w chouf")
    elif not options.newmac:
        parser.error("L'adresse mac kho mamditehanach dir --help w chouf")
    return options

def change_mac(interface,newmac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] MAC adresse ta3 " + interface + " tbdlt l " + newmac + " ya les hommes")

def getOldmac(interface):
    ifconfigtext = subprocess.check_output(["ifconfig", interface])

    # good site to make regex rules pythex.org

    macold = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfigtext)

    # on fai lappel avec macold.group(0) car c un objet w hadak groupe raho tableau t3 wsh jana resultats
    if macold:
        return macold.group(0)
    else:
        print("m9drtch n9ra l'adresse MAC")

try:
    options = get_arguments()

    ancienmac=getOldmac(options.interface)

    if ancienmac:
        print("L'adresse mac l9dima hya : "+ancienmac)

    change_mac(options.interface, options.newmac)

    ancienmac=getOldmac(options.interface)
except KeyboardInterrupt:
    print("\n [-] rak 3abzt ctrl+c dok nquiti...   BOOM. lol ")
