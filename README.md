# Blockchain Legal Document Verification System

This project verifies legal documents using blockchain and IPFS.

## Features

- Document upload
- SHA256 integrity verification
- IPFS decentralized storage
- Blockchain metadata storage
- Document versioning
- User login and roles
- Blockchain explorer UI

## Technologies

- Python (Flask)
- Streamlit
- Solidity
- Hardhat
- Web3.py
- IPFS

---

# Setup

## 1 Install Node dependencies

npm install

## 2 Install Python dependencies

pip install -r requirements.txt

## 3 Start IPFS

ipfs daemon

## 4 Start local blockchain

npx hardhat node

## 5 Deploy smart contract

npx hardhat run scripts/deploy.js --network localhost

## 6 Start backend

cd backend
python app.py

## 7 Start UI

streamlit run streamlit_app.py
