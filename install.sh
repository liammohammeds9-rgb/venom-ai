#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31m[!] Administrative alert: Please launch this installation script via sudo.\e[0m"
  exit 1
fi

echo -e "\e[34m[*] Commencing VENIOM AI Global Environment Setup...\e[0m"

# 1. Sync system package infrastructure
apt-get update -y && apt-get install -y python3-pip python3-scapy curl git

# 2. Bind Python library frameworks globally
pip3 install ollama --break-system-packages --quiet

# 3. Handle local Ollama system application deployment
if ! command -v ollama &> /dev/null; then
    echo -e "\e[32m[*] Extracting and staging core Ollama local binary services...\e[0m"
    curl -fsSL https://ollama.com | sh
    systemctl daemon-reload
    systemctl enable --now ollama
else
    echo -e "\e[34m[*] Core service binaries detected. Verifying active daemon process...\e[0m"
    systemctl start ollama
fi

# 4. Pull down the uncensored model directly to your disk
echo -e "\e[32m[*] Pulling Uncensored AI Matrix (llama3-gradient). Please remain connected to network...\e[0m"
ollama pull llama3-gradient

# 5. Map global command path routing
chmod +x venom.py
ln -sf "$(pwd)/venom.py" /usr/local/bin/veniom-ai

echo -e "\e[32m\n[+] VENIOM AI environment has successfully generated with zero errors!\e[0m"
echo -e "\e[34m[+] Call your autonomous engine from anywhere inside the terminal using: sudo veniom-ai\e[0m"
