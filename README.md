# Blockchain Legal Document Verification System

# Project Structure

```text
blockchain-legal-doc-verification/
│
├── backend/
│   ├── uploads/
│   ├── app.py
│   ├── blockchain.py
│   ├── hash_utils.py
│   └── ipfs_utils.py
│
├── contracts/
│   └── DocumentVerification.sol
│
├── scripts/
│   └── deploy.js
│
├── artifacts/
├── cache/
├── node_modules/
├── typechain-types/
│
├── streamlit_app.py
├── auth_config.py
├── hardhat.config.ts
├── package.json
├── package-lock.json
├── tsconfig.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Software Requirements

Install the following software before running the project.

| Software           | Purpose                    |
| ------------------ | -------------------------- |
| Python 3.10+       | Backend + Streamlit        |
| Node.js (LTS)      | Hardhat + Smart Contracts  |
| Git                | Clone repository           |
| IPFS (Kubo)        | Decentralized file storage |
| VS Code (Optional) | Development environment    |

---

# STEP 1 — Install Python

Download Python:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

While installing:

* Enable "Add Python to PATH"

Verify installation:

```bash
python --version
```

---

# STEP 2 — Install Node.js

Download Node.js LTS:

[https://nodejs.org/](https://nodejs.org/)

Verify installation:

```bash
node -v
npm -v
```

---

# STEP 3 — Install Git

Download Git:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

Verify installation:

```bash
git --version
```

---

# STEP 4 — Install IPFS (Kubo)

Download Kubo:

[https://dist.ipfs.tech/#kubo](https://dist.ipfs.tech/#kubo)

## Windows Setup

1. Download Windows AMD64 ZIP.
2. Extract ZIP.
3. Copy extracted folder to:

```text
C:\ipfs
```

4. Add this folder to System PATH.

Example:

```text
C:\ipfs
```

5. Restart terminal.

Verify installation:

```bash
ipfs version
```

---

# STEP 5 — Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/blockchain-legal-document-verification.git
```

Go inside project:

```bash
cd blockchain-legal-document-verification
```

---

# STEP 6 — Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

## Windows

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

---

# STEP 7 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# STEP 8 — Install Node Dependencies

```bash
npm install
```

This installs:

* Hardhat
* Ethers.js
* Solidity compiler
* Typechain
* Blockchain dependencies

---

# STEP 9 — Initialize IPFS

Run once:

```bash
ipfs init
```

---

# STEP 10 — Start IPFS Daemon

Open Terminal 1:

```bash
ipfs daemon
```

Expected output:

```text
Daemon is ready
```

Keep this terminal running.

---

# STEP 11 — Start Local Blockchain

Open Terminal 2:

```bash
npx hardhat node
```

Expected:

```text
Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/
```

Keep this terminal running.

---

# STEP 12 — Compile Smart Contracts

Open Terminal 3:

```bash
npx hardhat compile
```

---

# STEP 13 — Deploy Smart Contract

```bash
npx hardhat run scripts/deploy.js --network localhost
```

Example output:

```text
Contract deployed to:
0x5FbDB2315678afecb367f032d93F642f64180aa3
```

Copy this contract address.

---

# STEP 14 — Update Contract Address

Update BOTH files.

---

## backend/blockchain.py

Replace:

```python
contract_address = Web3.to_checksum_address("OLD_ADDRESS")
```

with:

```python
contract_address = Web3.to_checksum_address("NEW_ADDRESS")
```

---

## streamlit_app.py

Replace:

```python
CONTRACT_ADDRESS = "OLD_ADDRESS"
```

with:

```python
CONTRACT_ADDRESS = "NEW_ADDRESS"
```

---

# STEP 15 — Start Flask Backend

Open Terminal 4:

```bash
cd backend
python app.py
```

Backend starts at:

```text
http://127.0.0.1:5000
```

Keep terminal running.

---

# STEP 16 — Start Streamlit Frontend

Open Terminal 5:

```bash
streamlit run streamlit_app.py
```

Frontend opens at:

```text
http://localhost:8501
```

---

# Login Credentials

## Uploader Account

```text
Username: shrey
Password: shrey123
```

---

## Lawyer / Viewer Account

```text
Username: lawyer
Password: lawyer123
```

---

# Features Included

* Blockchain-based document verification
* IPFS decentralized storage
* SHA-256 integrity checking
* Role-based authentication
* Blockchain explorer
* Version tracking
* QR code generation
* Streamlit dashboard
* Flask backend APIs

---

# Running Order Checklist

Always start services in this order:

## 1. Start IPFS

```bash
ipfs daemon
```

## 2. Start Hardhat Blockchain

```bash
npx hardhat node
```

## 3. Deploy Smart Contract

```bash
npx hardhat run scripts/deploy.js --network localhost
```

## 4. Update Contract Address

* backend/blockchain.py
* streamlit_app.py

## 5. Start Flask Backend

```bash
cd backend
python app.py
```

## 6. Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# Common Commands

## Recompile Contracts

```bash
npx hardhat compile
```

---

## Redeploy Contracts

```bash
npx hardhat run scripts/deploy.js --network localhost
```

---

## Stop Services

Use:

```text
CTRL + C
```

---

# Important Notes

## Hardhat Reset

Every time Hardhat node restarts:

* blockchain resets
* contract address changes
* contracts must be redeployed
* contract address must be updated in:

  * backend/blockchain.py
  * streamlit_app.py

---

