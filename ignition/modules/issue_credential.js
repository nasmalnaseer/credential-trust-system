const hre = require("hardhat");

async function main() {
  // Use the exact hash (ensure NO spaces)
  const credentialHash = "0x76c78a28719fe110a83e24c57b8cc7be9bdcd1077d27da32dab05759cbdcdd4d"; 
  const studentName = "John Doe"; // From your OCR test
  const degreeType = "Bachelor of Blockchain"; // From your OCR test

  const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3"; 

  const DegreeVerifier = await hre.ethers.getContractAt("DegreeVerifier", contractAddress);

  console.log("Issuing credential...");
  
  // Notice we now pass 3 arguments to match your Solidity function!
  const tx = await DegreeVerifier.issueDegree(credentialHash, studentName, degreeType);
  
  await tx.wait();

  console.log("✅ Success! Credential has been recorded on the blockchain.");
  console.log(`Transaction Hash: ${tx.hash}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});