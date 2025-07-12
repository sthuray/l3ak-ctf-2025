#!/bin/bash

WORDLIST="rockyou.txt"

if [ ! -f "$WORDLIST" ]; then
  curl -sL https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -o "$WORDLIST"
  if [ $? -ne 0 ]; then
    echo "Failed to download rockyou.txt. Exiting."
    exit 1
  fi
fi

hashcat -m 0 -a 0 hashes.txt "$WORDLIST"
hashcat -m 0 -a 0 hashes.txt "$WORDLIST" --show > hashes.out
