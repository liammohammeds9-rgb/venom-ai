#!/bin/sh
set -e
echo ">>> Downloading Ollama installation binary package..."
curl -fsSL https://ollama.com -o ollama.tgz
echo ">>> Extracting Ollama core system binaries..."
sudo tar -C /usr -xzf ollama.tgz
echo ">>> Setting local execution access controls..."
sudo chmod +x /usr/bin/ollama
echo "[+] Ollama application framework installed successfully!"
