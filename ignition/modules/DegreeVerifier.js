const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

module.exports = buildModule("DegreeVerifierModule", (m) => {
  // This tells Ignition to deploy the "DegreeVerifier" contract
  const verifier = m.contract("DegreeVerifier");

  return { verifier };
});