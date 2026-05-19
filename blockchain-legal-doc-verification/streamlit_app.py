import streamlit as st
import requests
from web3 import Web3
import json
import pandas as pd
from datetime import datetime
import streamlit_authenticator as stauth
from auth_config import credentials
import os
import qrcode
from io import BytesIO

st.set_page_config(
    page_title="TrustChain",
    layout="wide"
)

API_URL = "http://127.0.0.1:5000"
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# -----------------------------
# Authentication Setup
# -----------------------------

authenticator = stauth.Authenticate(
    credentials,
    "document_app_cookie",
    "abcdef1234567890abcdef1234567890",
    cookie_expiry_days=1
)

authenticator.login(location="main")

authentication_status = st.session_state.get("authentication_status")
username = st.session_state.get("username")
name = st.session_state.get("name")

# -----------------------------
# Authentication Logic
# -----------------------------

if authentication_status is False:
    st.error("Username/password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")

elif authentication_status:

    st.sidebar.success(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")

    role = credentials["usernames"][username]["role"]

    st.title("TrustChain")
    st.subheader("Decentralized Legal Document Verification Using Blockchain and IPFS")

    # -----------------------------
    # Blockchain Connection
    # -----------------------------

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    contract_address = Web3.to_checksum_address(CONTRACT_ADDRESS)

    abi_path = os.path.join(
        "artifacts",
        "contracts",
        "DocumentVerification.sol",
        "DocumentVerification.json"
    )

    if not os.path.exists(abi_path):
        st.error("Contract not compiled. Run: npx hardhat compile")
        st.stop()

    with open(abi_path) as f:
        abi = json.load(f)["abi"]

    contract = w3.eth.contract(address=contract_address, abi=abi)

    docs = contract.functions.getDocuments().call()

    # -----------------------------
    # DASHBOARD
    # -----------------------------

    st.markdown("## Dashboard")

    total_docs = len(docs)

    uploaders = set()
    total_versions = 0

    latest_upload = "N/A"

    if total_docs > 0:
        latest_upload = docs[-1][0]

    for d in docs:
        uploaders.add(d[4])
        total_versions += d[5]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Documents", total_docs)
    col2.metric("Total Uploaders", len(uploaders))
    col3.metric("Total Versions", total_versions)
    col4.metric(
        "Blockchain Status",
        "Connected" if w3.is_connected() else "Disconnected"
    )

    st.markdown("---")

    st.info(f"Latest Upload: {latest_upload}")

    # -----------------------------
    # Navigation
    # -----------------------------

    if role == "uploader":
        options = [
            "Upload Document",
            "Verify Document",
            "Blockchain Explorer"
        ]
    else:
        options = [
            "Verify Document",
            "Blockchain Explorer"
        ]

    option = st.sidebar.selectbox("Navigation", options)

    # -----------------------------------
    # Upload Document
    # -----------------------------------

    if option == "Upload Document":

        st.header("Upload Document to Blockchain")

        file = st.file_uploader("Choose a file")

        if file is not None:

            if st.button("Upload"):

                try:

                    response = requests.post(
                        f"{API_URL}/upload",
                        files={"file": file}
                    )

                    data = response.json()

                    st.success("Document stored successfully")

                    st.write("### Blockchain Details")

                    st.write("Document Hash:", data.get("hash"))
                    st.write("IPFS CID:", data.get("ipfs_cid"))
                    st.write("Version:", data.get("version"))
                    st.write("Transaction:", data.get("transaction"))

                    ipfs_link = f"http://127.0.0.1:8080/ipfs/{data.get('ipfs_cid')}"

                    st.markdown(
                        f"[Open File from IPFS]({ipfs_link})"
                    )

                    # -----------------------------
                    # QR CODE GENERATION
                    # -----------------------------

                    st.write("### QR Code Verification")

                    qr = qrcode.make(ipfs_link)

                    buf = BytesIO()
                    qr.save(buf)

                    st.image(buf)

                    st.caption(
                        "Scan QR code to open document from decentralized IPFS storage"
                    )

                except Exception as e:
                    st.error(f"Upload failed: {e}")

    # -----------------------------------
    # Verify Document
    # -----------------------------------

    elif option == "Verify Document":

        st.header("Verify Document Integrity")

        file = st.file_uploader("Upload document for verification")

        if file is not None:

            if st.button("Verify"):

                try:

                    response = requests.post(
                        f"{API_URL}/verify",
                        files={"file": file}
                    )

                    result = response.json()

                    if result.get("status") == "verified":

                        st.success("Document Verified - Integrity Intact")

                        st.write("### Verification Details")

                        st.write("IPFS CID:", result.get("ipfs_cid"))
                        st.write("Version:", result.get("version"))

                    else:
                        st.error("Document Tampered or Not Found")

                except Exception as e:
                    st.error(f"Verification failed: {e}")

    # -----------------------------------
    # Blockchain Explorer
    # -----------------------------------

    elif option == "Blockchain Explorer":

        st.header("Blockchain Stored Documents")

        try:

            records = []

            for d in docs:

                records.append({
                    "File Name": d[0],
                    "Hash": d[1],
                    "IPFS CID": d[2],
                    "Timestamp": datetime.fromtimestamp(d[3]),
                    "Uploader": d[4],
                    "Version": d[5],
                    "IPFS Link": f"http://127.0.0.1:8080/ipfs/{d[2]}"
                })

            if len(records) == 0:
                st.info("No documents stored yet")

            else:

                df = pd.DataFrame(records)

                st.dataframe(df, use_container_width=True)

                st.write("### Open Document from IPFS")

                selected = st.selectbox(
                    "Select Document CID",
                    df["IPFS CID"]
                )

                if selected:

                    st.markdown(
                        f"[Open File](http://127.0.0.1:8080/ipfs/{selected})"
                    )

        except Exception as e:
            st.error(f"Blockchain connection failed: {e}")