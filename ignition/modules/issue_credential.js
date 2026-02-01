const hre = require("hardhat");

async function main() {
  // Replace this with the 0x hash you just copied from your Python script!
  const credentialHash = "x76c78a28719fe110a83e24c57b8cc7be9bdcd1077d27da32dab05759cbdcdd4d"; 
  const studentAddress = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266"; // Hardhat Account #0

  // The address where your contract was deployed (from your deployment logs)
  const contractAddress = "0x5fbdb2315678afecb367f032d93f642f64180aa3"; 

  const DegreeVerifier = await hre.ethers.getContractAt("DegreeVerifier", contractAddress);

  console.log("Issuing credential...");
  const tx = await DegreeVerifier.issueDegree(studentAddress, credentialHash);
  await tx.wait();

  console.log("✅ Success! Credential has been recorded on the blockchain.");
  console.log(`Transaction Hash: ${tx.hash}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});