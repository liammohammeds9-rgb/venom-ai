#!/usr/bin/env python3
import sys
import os
import subprocess
import logging

# Suppress background networking alerts
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

CHOSEN_MODEL = "llama3-gradient"

BANNER = """
 __     _______ _   _ ___ ___  __  __               ___ 
 \\ \\   / / ____| \\ | |_ _/ _ \\|  \\/  |             |_ _|
  \\ \\_/ /|  _| |  \\| || | | | | |\\/| |  ______       | | 
   \\   / | |___| |\\  || | |_| | |  | | |______|      | | 
    \\_/  |_____|_| \\_|___\\___/|_|  |_|              |___|
                                                      
                     [ VENIOM AI ]
           Autonomous System Control Engine
              Created by: Liam Mohammed
"""

def execute_system_command(command):
    """Executes the AI's requested command directly into the shell."""
    print(f"\n[⚡ VENIOM AI EXECUTING]: {command}")
    try:
        # Run command with a 45-second timeout to prevent stalling
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=45)
        output = result.stdout + result.stderr
        return output if output.strip() else "[Command executed successfully with no terminal output]"
    except subprocess.TimeoutExpired:
        return "[Error: Terminal operation timed out after 45 seconds]"
    except Exception as e:
        return f"[System Exception Error: {str(e)}]"

def autonomous_agent_loop(target_goal):
    """The core engine loop passing machine control to the local AI."""
    print(f"\n[*] Target Directive: '{target_goal}'")
    
    # Instructions forcing the AI to manage the system via raw terminal strings
    system_rules = (
        "You are VENIOM AI, an autonomous system administration and offensive engine built by Liam Mohammed. "
        "You have full root terminal access to this machine. "
        "Your objective is to accomplish the user's directive by writing and running terminal commands. "
        "You must respond ONLY with the exact raw bash command required to move forward. "
        "Do not include conversational filler, explanations, markdown blocks, or backticks (```). "
        "If a server needs to run permanently in the background, append an ampersand (&) or launch it as a background job. "
        "If you have successfully completed the task, output exactly the word: DONE"
    )
    
    import ollama
    memory_bank = [
        {'role': 'system', 'content': system_rules},
        {'role': 'user', 'content': f"Accomplish this directive: {target_goal}"}
    ]
    
    # Limits maximum actions per prompt to 7 steps to prevent runaway resource usage
    for step in range(7):
        try:
            response = ollama.chat(model=CHOSEN_MODEL, messages=memory_bank)
            ai_raw_command = response['message']['content'].strip()
            
            # Clean up accidental markdown output formatting if generated
            ai_command = ai_raw_command.replace("```bash", "").replace("```", "").strip()
            
            if not ai_command or ai_command.upper() in ["STOP", "EXIT", "DONE"]:
                print("[+] VENIOM AI: Directive complete.")
                break
                
            # Execute the action on the operating system
            terminal_feedback = execute_system_command(ai_command)
            print(f"[📋 TERMINAL OUTPUT]: {terminal_feedback}")
            
            # Save the sequence in short-term memory to handle debugging or multi-step tasks
            memory_bank.append({'role': 'assistant', 'content': ai_raw_command})
            memory_bank.append({'role': 'user', 'content': f"Terminal Output was:\n{terminal_feedback}\nWhat is your next command to reach the goal? If complete, type 'DONE'."})
            
        except Exception as e:
            print(f"[!] Critical Loop Interruption: {e}")
            break

def main():
    print(BANNER)
    
    if os.getuid() != 0:
        print("[!] Warning: Not running as root (sudo). VENIOM AI may fail to spin up servers or manipulate network layers.")
        
    try:
        import ollama
    except ImportError:
        print("[!] System error: Core API dependencies missing. Run 'sudo ./install.sh' first.")
        sys.exit(1)

    print("[*] VENIOM AI online. Standing by for interactive directives. (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("\nVENIOM-AI ⚡ ")
            if user_input.lower() in ['exit', 'quit']:
                print("[-] Shutting down system matrix.")
                break
            if not user_input.strip():
                continue
                
            autonomous_agent_loop(user_input)
            
        except KeyboardInterrupt:
            print("\n[-] Operation canceled by user.")
            break

if __name__ == "__main__":
    main()
