// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

interface ILexGuard {
    struct RuleProof {
        bytes32 ruleSetHash;
        uint256 timestamp;
        uint256 expiration;
        bytes signature;
    }

    event RuleSetVerified(bytes32 indexed ruleSetHash, address indexed verifier, uint256 timestamp);
    event ComplianceBreachReverted(address indexed caller, bytes32 indexed ruleSetHash, string reason);

    function verifyAndEnforce(bytes32 ruleSetHash, RuleProof calldata proof) external view returns (bool);
    function isJurisdictionCompliant(address targetContract, bytes4 functionSelector) external view returns (bool);
}
