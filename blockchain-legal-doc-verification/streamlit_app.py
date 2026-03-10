import streamlit as st
import requests
from web3 import Web3
import json
import pandas as pd
from datetime import datetime
import streamlit_authenticator as stauth
from auth_config import credentials

st.set_page_config(page_title="Blockchain Document Verification", layout="wide")

API_URL = "http://127.0.0.1:5000"
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# -----------------------------
# Authentication Setup
# -----------------------------

authenticator = stauth.Authenticate(
    credentials,
    "document_app_cookie",
    "abcdef1234567890abcdef1234567890",  # >= 32 chars
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

    st.title("Blockchain Legal Document Verification System")

    # Role-based navigation
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
    # Upload Document (Uploader only)
    # -----------------------------------

    if option == "Upload Document":

        st.header("Upload Document to Blockchain")

        file = st.file_uploader("Choose a file")

        if file is not None:

            if st.button("Upload"):

                response = requests.post(
                    f"{API_URL}/upload",
                    files={"file": file}
                )

                data = response.json()

                st.success("Document stored successfully")

                st.write("### Blockchain Details")

                st.write("Document Hash:", data["hash"])
                st.write("IPFS CID:", data["ipfs_cid"])
                st.write("Version:", data["version"])
                st.write("Transaction:", data["transaction"])

                st.markdown(
                    f"[Open File from IPFS](http://127.0.0.1:8080/ipfs/{data['ipfs_cid']})"
                )

    # -----------------------------------
    # Verify Document
    # -----------------------------------

    elif option == "Verify Document":

        st.header("Verify Document Integrity")

        file = st.file_uploader("Upload document for verification")

        if file is not None:

            if st.button("Verify"):

                response = requests.post(
                    f"{API_URL}/verify",
                    files={"file": file}
                )

                result = response.json()

                if result["status"] == "verified":
                    st.success("Document Verified - Integrity Intact")
                else:
                    st.error("Document Tampered - Not Found on Blockchain")

                st.write(result)

    # -----------------------------------
    # Blockchain Explorer
    # -----------------------------------

    elif option == "Blockchain Explorer":

        st.header("Blockchain Stored Documents")

        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        contract_address = Web3.to_checksum_address(CONTRACT_ADDRESS)

        with open(
            "../blockchain/artifacts/contracts/DocumentVerification.sol/DocumentVerification.json"
        ) as f:
            abi = json.load(f)["abi"]

        contract = w3.eth.contract(address=contract_address, abi=abi)

        docs = contract.functions.getDocuments().call()

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

            selected = st.selectbox("Select Document CID", df["IPFS CID"])

            if selected:
                st.markdown(
                    f"[Open File](http://127.0.0.1:8080/ipfs/{selected})"
                )