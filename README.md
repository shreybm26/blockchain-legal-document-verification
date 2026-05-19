# Blockchain Legal Document Verification System

A decentralized legal document verification system built using:

- Ethereum Blockchain
- Solidity Smart Contracts
- IPFS (InterPlanetary File System)
- Flask Backend
- Streamlit Frontend
- SHA-256 Cryptographic Hashing

---

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

# Features

- Blockchain-based document verification
- IPFS decentralized storage
- SHA-256 integrity verification
- Role-based authentication
- Blockchain explorer dashboard
- Version tracking
- QR code generation
- Streamlit web interface
- Flask backend APIs

---

# Software Requirements

Install the following software before running the project.

| Software | Purpose |
|---|---|
| Python 3.10+ | Backend + Streamlit |
| Node.js (LTS) | Hardhat + Smart Contracts |
| Git | Clone repository |
| IPFS (Kubo) | Decentralized file storage |
| VS Code (Optional) | Development environment |

---

# STEP 1 — Install Python

Download Python:

https://www.python.org/downloads/

While installing:

- Enable **"Add Python to PATH"**

Verify installation:

```bash
python --version
```

---

# STEP 2 — Install Node.js

Download Node.js LTS:

https://nodejs.org/

Verify installation:

```bash
node -v
npm -v
```

---

# STEP 3 — Install Git

Download Git:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

---

# STEP 4 — Install IPFS (Kubo)

Download Kubo:

https://dist.ipfs.tech/#kubo

## Windows Setup

1. Download the Windows AMD64 ZIP.
2. Extract the ZIP file.
3. Copy the extracted folder to:

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

Example output:

```text
ipfs version 0.40.1
```

---

# STEP 5 — Clone Repository

```bash
git clone https://github.com/shreybm26/blockchain-legal-document-verification.git
```

Go inside the project:

```bash
cd blockchain-legal-document-verification
```

---

# STEP 6 — Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment.

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

- Hardhat
- Ethers.js
- Solidity compiler
- Typechain
- Blockchain dependencies

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

Expected output:

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

Copy this contract address carefully.

---

# STEP 14 — Update Contract Address

After deploying the smart contract, you MUST update the contract address in 2 files.

---

## File 1 — backend/blockchain.py

Open:

```text
backend/blockchain.py
```

Find this line:

```python
contract_address = Web3.to_checksum_address("OLD_ADDRESS")
```

Replace it with:

```python
contract_address = Web3.to_checksum_address(
    "0x5FbDB2315678afecb367f032d93F642f64180aa3"
)
```

---

## File 2 — streamlit_app.py

Open:

```text
streamlit_app.py
```

Find this line:

```python
CONTRACT_ADDRESS = "OLD_ADDRESS"
```

Replace it with:

```python
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
```

Save both files after updating.

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

## Legal Officer Account

```text
Username: lawyer
Password: password123
```

Permissions:
- Upload documents
- Verify documents
- Access blockchain explorer

---

## Client Account

```text
Username: client
Password: password256
```

Permissions:
- Verify documents
- Access blockchain explorer

---

# Running Order Checklist

Always start services in this order.

## 1. Start IPFS

```bash
ipfs daemon
```

---

## 2. Start Hardhat Blockchain

```bash
npx hardhat node
```

---

## 3. Deploy Smart Contract

```bash
npx hardhat run scripts/deploy.js --network localhost
```

---

## 4. Update Contract Address

Update BOTH files:
- backend/blockchain.py
- streamlit_app.py

---

## 5. Start Flask Backend

```bash
cd backend
python app.py
```

---

## 6. Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# Open the Application

Frontend:

```text
http://localhost:8501
```

Backend:

```text
http://127.0.0.1:5000
```

---

# Common Commands

## Recompile Smart Contracts

```bash
npx hardhat compile
```

---

## Redeploy Smart Contract

```bash
npx hardhat run scripts/deploy.js --network localhost
```

---

## Stop Running Services

Use:

```text
CTRL + C
```

---

# Important Notes

## Hardhat Reset

Every time Hardhat node restarts:

- blockchain resets
- contract address changes
- contracts must be redeployed
- contract address must be updated again

You MUST update:
- backend/blockchain.py
- streamlit_app.py

Otherwise the application will not work correctly.

---

# Troubleshooting

## If IPFS command does not work

Check if IPFS was added to PATH correctly.

Run:

```bash
ipfs version
```

---

## If Streamlit does not open

Run:

```bash
streamlit run streamlit_app.py
```

again.

---

## If verification fails

Check:
- IPFS daemon is running
- Hardhat node is running
- Smart contract was deployed
- Contract address was updated in BOTH files

---

# Recommended .gitignore

```gitignore
venv/
node_modules/
backend/uploads/
cache/
__pycache__/
*.pyc
*.zip
```

---

# Future Improvements

- MetaMask integration
- Public blockchain deployment
- Docker deployment
- AI-based fraud detection
- NFT-based ownership
- Mobile application
- Decentralized identity integration

---

# End of Documentation