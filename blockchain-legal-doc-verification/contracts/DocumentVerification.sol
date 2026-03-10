// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract DocumentVerification {

    struct Document {
        string fileName;
        string documentHash;
        string ipfsCID;
        uint256 timestamp;
        address uploader;
        uint256 version;
    }

    Document[] public documents;

    function storeDocument(
        string memory _fileName,
        string memory _hash,
        string memory _ipfsCID,
        uint256 _version
    ) public {

        documents.push(
            Document(
                _fileName,
                _hash,
                _ipfsCID,
                block.timestamp,
                msg.sender,
                _version
            )
        );
    }

    function getDocuments() public view returns (Document[] memory) {
        return documents;
    }

    function getDocumentCount() public view returns (uint256) {
        return documents.length;
    }
}