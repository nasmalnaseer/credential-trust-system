const hre = require("hardhat");

async function main() {
  // Use the same hash we issued earlier
  const credentialHash = "0x76c78a28719fe110a83e24c57b8cc7be9bdcd1077d27da32dab05759cbdcdd4d";
  const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

  const DegreeVerifier = await hre.ethers.getContractAt("DegreeVerifier", contractAddress);

  console.log("🔍 Verifying credential on the blockchain...");
  
  // This calls your 'verifyDegree' function from the Solidity contract
  const [isValid, studentName] = await DegreeVerifier.verifyDegree(credentialHash);

  if (isValid) {
    console.log("✅ VERIFIED: This is a legitimate degree!");
    console.log(`🎓 Student Name: ${studentName}`);
  } else {
    console.log("❌ NOT FOUND: This credential hash is invalid or hasn't been issued.");
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});