# 🔑 PassForge (`passforge`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![CSPRNG](https://img.shields.io/badge/Entropy-CSPRNG%20Cryptographic-green.svg)](https://github.com/MochErik/passforge)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange.svg)](https://github.com/MochErik/passforge)

> **High-Entropy Password, Diceware Passphrase & Crypto Token Generator CLI.** Generates cryptographically secure passwords, human-memorable multi-word Diceware passphrases, and raw hex/base64 tokens directly in your terminal.

---

## 🚀 Quick Install

```bash
pip install passforge
```

---

## 🖥️ Usage

### 1. Generate Standard Strong Password
```bash
passforge
# Output: 🔑 Generated Password: k9#mX2$vLp8@qW1z (Entropy: 95.2 bits | Very Strong)
```

### 2. Generate 4-Word Diceware Passphrase
```bash
passforge --phrase 4
# Output: 🔑 Diceware Passphrase: Falcon-Horizon-Crystal-Timber42 (Entropy: 51.2 bits | Very Strong)
```

### 3. Generate 32-Byte API Crypto Token
```bash
passforge --token 32
# Output: 4f8a3c9b2e1d0f5a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a
```

---

## 📜 License

MIT License © 2026 [Moch. Erik Irriansyah](https://github.com/MochErik)
