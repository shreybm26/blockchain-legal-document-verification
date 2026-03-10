from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

contract_address = Web3.to_checksum_address("0x5FbDB2315678afecb367f032d93F642f64180aa3")

with open("../artifacts/contracts/DocumentVerification.sol/DocumentVerification.json") as f:
    abi = json.load(f)["abi"]

contract = w3.eth.contract(address=contract_address, abi=abi)


def store_document(file_name, doc_hash, cid, version):

    tx = contract.functions.storeDocument(
        file_name,
        doc_hash,
        cid,
        version
    ).transact({
        "from": w3.eth.accounts[0]
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx)

    return receipt.transactionHash.hex()


def get_documents():

    return contract.functions.getDocuments().call()