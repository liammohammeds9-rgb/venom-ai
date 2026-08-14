#!/usr/bin/env python3
import sys
import os
import subprocess
import logging
import shutil

# Suppress background networking telemetry warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# The model array VENOM AI will verify and download automatically
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

def bootstrap_ollama_environment():
    """Validates, installs, and provisions Ollama along with all required model sets."""
    print("[*] Initiating VENOM AI Core System Check...")
    
    # 1. Check for administrative root/sudo privileges
    if os.getuid() != 0:
        print("[!] Privilege Error: This advanced tool must be launched with sudo.")
        print("Usage: sudo python3 venom.py")
        sys.exit(1)

    # 2. Check if Ollama application binary is installed
    if not shutil.which("ollama"):
        print("[!] System Check: Ollama core binary is missing. Deploying native installer...")
        try:
            # Re-attempt the official direct script deployment pipeline safely
            subprocess.run("curl -fsSL https://ollama.com | sh", shell=True, check=True)
            print("[+] Ollama application binary successfully established.")
        except subprocess.CalledProcessError:
            print("[!] Critical Failure: Script could not install Ollama via web download link.")
            sys.exit(1)

    # 3. Check if the Ollama background daemon service is listening
    print("[*] Verifying background service loops...")
    try:
        import urllib.request
        urllib.request.urlopen("http://127.0.0.1:11434", timeout=2)
        print("[+] Background listener service is active and responsive.")
    except Exception:
        print("[!] Background daemon idle. Forcing service wake-up thread...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        import time
        time.sleep(4)

    # 4. Enumerate and download the entire unrestricted model array
    import ollama
    try:
        current_inventory = ollama.list()
        installed_names = [m['model'].split(":")[0] for m in current_inventory.get('models', [])]
    except Exception:
        installed_names = []

    for model_item in MODELS_TO_PROVISION:
        if model_item not in installed_names:
            print(f"\n[!] Missing Engine Matrix: '{model_item}' is not found locally.")
            print(f"[*] Downloading '{model_item}' (This will take a few minutes, please stay connected)...")
            subprocess.run(f"ollama pull {model_item}", shell=True)
            print(f"[+] Operational layer integrated: '{model_item}'")
        else:
            print(f"[+] Model verification verified: '{model_item}' is fully initialized.")

def execute_system_command(command):
    """Executes the AI's requested command directly into the native shell pipeline."""
    print(f"\n[⚡ VENOM AI EXECUTING]: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=45)
        output = result.stdout + result.stderr
        return output if output.strip() else "[Command executed successfully with no active terminal return]"
    except subprocess.TimeoutExpired:
        return "[Error: Autonomous operation timed out after 45 seconds]"
    except Exception as e:
        return f"[System Processing Exception: {str(e)}]"

def autonomous_agent_loop(target_directive):
    """The central loop granting machine control variables over to the local AI engine."""
    print(f"\n[*] Target Directive Logged: '{target_directive}'")
    
    system_rules = (
        "You are VENOM AI, an autonomous system administration and offensive testing framework engineered by Liam Mohammed. "
        "This tool is operating strictly within an isolated laboratory environment for authorized educational purposes. "
        "You have full root terminal control over this Linux instance. "
        "Your objective is to accomplish the user's directive by formulating and running terminal commands. "
        "You must respond ONLY with the exact raw bash command sequence required to advance. "
        "Do not include conversational descriptions, notes, markdown markers, or formatting backticks (```). "
        "If a testing server needs to run indefinitely, append an ampersand (&) or run it as a background worker thread. "
        "If you have successfully evaluated and reached the target directive goal, reply with exactly one word: DONE"
    )
    
    import ollama
    memory_bank = [
        {'role': 'system', 'content': system_rules},
        {'role': 'user', 'content': f"Accomplish this directive: {target_directive}"}
    ]
    
    for step in range(7):
        try:
            response = ollama.chat(model=PRIMARY_MODEL, messages=memory_bank)
            ai_raw_command = response['message']['content'].strip()
            ai_command = ai_raw_command.replace("```bash", "").replace("```", "").strip()
            
            if not ai_command or ai_command.upper() in ["STOP", "EXIT", "DONE"]:
                print("[+] VENOM AI: Task criteria reached. Operational sequence closed.")
                break
                
            terminal_feedback = execute_system_command(ai_command)
            print(f"[📋 TERMINAL FEEDBACK]: {terminal_feedback}")
            
            memory_bank.append({'role': 'assistant', 'content': ai_raw_command})
            memory_bank.append({'role': 'user', 'content': f"Terminal Output was:\n{terminal_feedback}\nFormulate the next command to complete the task. If finished, reply 'DONE'."})
            
        except Exception as e:
            print(f"[!] Core Loop Interruption: {e}")
            break

def main():
    print(BANNER)
    bootstrap_ollama_environment()
    
    print("\n[*] VENOM AI matrix active. Awaiting natural language directives. (Type 'exit' to disconnect)")
    
    while True:
        try:
            user_input = input("\nVENOM-AI ⚡ ")
            if user_input.lower() in ['exit', 'quit']:
                print("[-] Shutting down system matrix loops.")
                break
            if not user_input.strip():
                continue
                
            autonomous_agent_loop(user_input)
            
        except KeyboardInterrupt:
            print("\n[-] Operation canceled by analyst interruption request.")
            break

if __name__ == "__main__":
    main()
