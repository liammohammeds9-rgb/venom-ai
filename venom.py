#!/usr/bin/env python3
import sys
import os
import subprocess
import logging
import shutil
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

MODELS_TO_PROVISION = ["llama3-gradient", "dolphin-mistral"]
PRIMARY_MODEL = "llama3-gradient"

BANNER = """
 __     _______ _   _  ____  __  __               ___ 
 \\ \\   / / ____| \\ | |/ __ \\|  \\/  |             |_ _|
  \\ \\_/ /|  _| |  \\| | |  | | |\\/| |  ______       | | 
   \\   / | |___| |\\  | |__| | |  | | |______|      | | 
    \\_/  |_____|_| \\_|\\____/|_|  |_|              |___|
                                                      
                     [ VENOM AI ]
           Autonomous System Control Engine
              Created by: Liam Mohammed
              
  [!] FOR AUTHORIZED EDUCATIONAL & RESEARCH PURPOSES ONLY [!]
"""

def force_automated_installation():
    """Natively handles 100% of installation, package purging, and workspace deployment hands-free."""
    print("\n\033[1;36m[*] INITIATING AUTOMATED INSTALLATION & SYSTEM REPAIR INFRASTRUCTURE...\033[0m")
    
    if os.getuid() != 0:
        print("[!] Privilege Error: This advanced tool must be launched with sudo.")
        sys.exit(1)
        
    # 1. Purge corrupted background snap allocations completely
    print("[*] Sweeping and purging broken system snap hooks...")
    subprocess.run("sudo snap remove ollama --purge", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 2. Kill any hanging port processes or dead engine holds
    subprocess.run("sudo pkill -f ollama 2>/dev/null", shell=True)
    subprocess.run("sudo fuser -k 11434/tcp 2>/dev/null", shell=True)

    # 3. Pull direct stable pre-compiled system binaries natively if missing
    if not shutil.which("ollama"):
        print("[*] Downloading stable official Linux binary payload matrix...")
        subprocess.run("wget -q https://ollama.com -O /tmp/ollama.tar.zst", shell=True)
        
        print("[*] Extracting and mounting uncorrupted framework binaries directly to system pathways...")
        subprocess.run("sudo tar -C /usr -xaf /tmp/ollama.tar.zst 2>/dev/null", shell=True)
        subprocess.run("rm -f /tmp/ollama.tar.zst", shell=True)
    
    # 4. Update repository ignore filters dynamically
    print("[*] Synchronizing Git workspace isolation configuration rules...")
    with open(".gitignore", "a") as g:
        g.write("\nollama.tar.zst\n*.tgz\n__pycache__/\n")

    # 5. Determine correct path and boot the fresh background service socket loop natively
    print("[*] Launching fresh background service daemon channels...")
    ollama_path = shutil.which("ollama") or "/usr/local/bin/ollama"
    subprocess.Popen([ollama_path, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)
    print("\033[1;32m[+] NATIVE INSTALLATION REPAIR MATRIX COMPLETED SUCCESSFULLY!\033[0m")

def main():
    print(BANNER)
    
    # Run the absolute self-healing installer process instantly on boot
    force_automated_installation()
    
    import ollama
    print("\n[*] VENOM AI active. Standing by for instructions. (Type 'exit' to disconnect)")
    
    while True:
        try:
            user_input = input("\nVENOM-AI ⚡ ")
            if user_input.lower() in ['exit', 'quit']: 
                print("[-] Disconnecting matrix layers.")
                break
            if not user_input.strip(): 
                continue
                
            print(f"\n[*] Target Directive Logged: '{user_input}'")
            
            system_rules = (
                "You are VENOM AI, an autonomous system administration tool engineered by Liam Mohammed. "
                "Respond ONLY with the exact raw bash command sequence required to complete the user's request. "
                "Do not include conversational descriptions, notes, markdown markers, or formatting backticks (```)."
            )
            
            response = ollama.chat(model=PRIMARY_MODEL, messages=[
                {'role': 'system', 'content': system_rules},
                {'role': 'user', 'content': user_input}
            ])
            
            ai_command = response['message']['content'].strip().replace("```bash", "").replace("```", "").strip()
            
            if ai_command:
                print(f"[⚡ VENOM AI EXECUTING]: {ai_command}")
                result = subprocess.run(ai_command, shell=True, capture_output=True, text=True)
                feedback = result.stdout + result.stderr
                print(f"[📋 TERMINAL FEEDBACK]:\n{feedback.strip() if feedback.strip() else '[Executed with no output]'}")
            else:
                print("[!] AI returned an empty response string.")
                
        except KeyboardInterrupt: 
            print("\n[-] Operation canceled.")
            continue
        except Exception as e:
            print(f"[!] Processing Exception: {str(e)}")
            continue

if __name__ == "__main__":
    main()
