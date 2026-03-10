from flask import Flask, request, jsonify
import os

from hash_utils import generate_hash
from blockchain import store_document
from ipfs_utils import upload_to_ipfs
from blockchain import store_document, get_documents

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

document_versions = {}

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc_hash = generate_hash(path)

    cid = upload_to_ipfs(path)

    # get existing documents from blockchain
    docs = get_documents()

    version = 1

    for d in docs:
        if d[0] == file.filename:
            version += 1

    tx_hash = store_document(
        file.filename,
        doc_hash,
        cid,
        version
    )

    return jsonify({
        "message": "Document stored",
        "hash": doc_hash,
        "ipfs_cid": cid,
        "version": version,
        "transaction": tx_hash
    })

@app.route("/verify", methods=["POST"])
def verify():

    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc_hash = generate_hash(path)

    # get stored documents
    docs = get_documents()

    for d in docs:
        if d[1] == doc_hash:
            return jsonify({
                "status": "verified",
                "message": "Document exists on blockchain",
                "ipfs_cid": d[2],
                "version": d[5]
            })

    return jsonify({
        "status": "tampered",
        "message": "Document not found on blockchain"
    })

if __name__ == "__main__":
    app.run(debug=True)