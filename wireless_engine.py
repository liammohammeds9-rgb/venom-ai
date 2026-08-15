#!/usr/bin/env python3
import os
import sys
import subprocess
import time

def check_monitor_mode(interface):
    """Verifies or activates monitor mode on the designated testing adapter."""
    print(f"[*] Analyzing interface status for: {interface}")
    status = subprocess.run(f"iwconfig {interface}", shell=True, capture_output=True, text=True)
    if "Mode:Monitor" not in status.stdout:
        print(f"[*] Activating monitor mode on {interface}...")
        subprocess.run(f"sudo ip link set {interface} down", shell=True)
        subprocess.run(f"sudo iw set {interface} mode monitor", shell=True)
        subprocess.run(f"sudo ip link set {interface} up", shell=True)
    print(f"[+] Interface {interface} is verified in Monitor Mode.")

def live_spectrum_scan(interface):
    """Invokes airodump-ng to map nearby wireless access points."""
    print(f"\n[*] Initializing live radio frequency scan on {interface}...")
    print("[!] PRESS CTRL+C TO STOP SCANNING ONCE TARGET IS IDENTIFIED [!]\n")
    time.sleep(2)
    try:
        subprocess.run(f"sudo airodump-ng {interface}", shell=True)
    except KeyboardInterrupt:
        print("\n[+] Scan paused. Target identification locked.")

def deploy_wireless_framework(interface, ssid, channel, clone_bssid=None):
    """Generates hostapd and dnsmasq parameters to establish the wireless gateway."""
    print(f"\n[*] Compiling system profiles for SSID: '{ssid}' on Channel: {channel}...")
    
    hostapd_template = f"""
interface={interface}
driver=nl80211
ssid={ssid}
hw_mode=g
channel={channel}
auth_algs=1
wmm_enabled=0
"""
    if clone_bssid:
        hostapd_template += f"bssid={clone_bssid}\n"
        print(f"[*] Mirroring target hardware MAC address: {clone_bssid}")

    with open("/tmp/venom_hostapd.conf", "w") as f:
        f.write(hostapd_template.strip())

    dnsmasq_template = f"""
interface={interface}
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
address=/#/10.0.0.1
"""
    with open("/tmp/venom_dnsmasq.conf", "w") as f:
        f.write(dnsmasq_template.strip())

    print("[+] Configuration infrastructure files written to /tmp/")
    print("[*] Ready for deployment via system daemons.")

def main():
    if os.getuid() != 0:
        print("[!] Error: Administrative privileges (sudo) required for raw hardware hooks.")
        sys.exit(1)
        
    print("--- VENOM AI WIRELESS TESTING MATRIX ---")
    interface = input("Enter wireless interface name (e.g., wlan0): ").strip()
    
    check_monitor_mode(interface)
    
    print("\nSelect Operational Mode:")
    print("1) Scan environment and clone an existing network")
    print("2) Build an entirely new custom open testing network")
    choice = input("Option > ").strip()
    
    if choice == "1":
        live_spectrum_scan(interface)
        print("\n--- Enter Target Details observed from the scan ---")
        ssid = input("Target SSID Name: ").strip()
        channel = input("Target Channel Number: ").strip()
        bssid = input("Target BSSID (MAC Address): ").strip()
        deploy_wireless_framework(interface, ssid, channel, clone_bssid=bssid)
    else:
        ssid = input("Enter new custom network SSID name: ").strip()
        channel = input("Enter channel number (1-11): ").strip()
        deploy_wireless_framework(interface, ssid, channel)

if __name__ == "__main__":
    main()
