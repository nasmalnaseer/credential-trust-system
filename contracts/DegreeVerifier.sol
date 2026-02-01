// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract DegreeVerifier {
    address public owner;

    struct Certificate {
        string studentName;
        string degreeType;
        uint256 dateIssued;
        bool isValid;
    }

    // Mapping of a unique Hash (from AI/IPFS) to Certificate details
    mapping(bytes32 => Certificate) public certificates;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the university can issue degrees");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // Function to add a new degree hash
    function issueDegree(
        bytes32 _degreeHash, 
        string memory _name, 
        string memory _degree
    ) public onlyOwner {
        certificates[_degreeHash] = Certificate(_name, _degree, block.timestamp, true);
    }

    // Function to verify if a hash exists
    function verifyDegree(bytes32 _degreeHash) public view returns (bool, string memory) {
        if (certificates[_degreeHash].isValid) {
            return (true, certificates[_degreeHash].studentName);
        }
        return (false, "Degree not found or invalid");
    }
}