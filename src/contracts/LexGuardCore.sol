// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

import "./ILexGuard.sol";

/**
 * @title LexGuardCore
 * @notice On-chain formal verification enforcement and EIP-712 proof validator.
 */
contract LexGuardCore is ILexGuard {
    address public sovereignAuditor;
    mapping(bytes32 => bool) public activeRuleSets;
    mapping(address => mapping(bytes4 => bool)) public frozenActions;

    bytes32 public constant EIP712_DOMAIN_TYPEHASH = keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)");
    bytes32 public constant PROOF_TYPEHASH = keccak256("RuleProof(bytes32 ruleSetHash,uint256 timestamp,uint256 expiration)");

    modifier onlyAuditor() {
        require(msg.sender == sovereignAuditor, "LexGuard: Caller is not sovereign auditor");
        _;
    }

    constructor(address _auditor) {
        require(_auditor != address(0), "Invalid auditor");
        sovereignAuditor = _auditor;
    }

    function verifyAndEnforce(bytes32 ruleSetHash, RuleProof calldata proof) external view override returns (bool) {
        require(block.timestamp <= proof.expiration, "LexGuard: Proof expired");
        require(proof.ruleSetHash == ruleSetHash, "LexGuard: Hash mismatch");

        bytes32 structHash = keccak256(abi.encode(PROOF_TYPEHASH, proof.ruleSetHash, proof.timestamp, proof.expiration));
        bytes32 domainSeparator = keccak256(abi.encode(EIP712_DOMAIN_TYPEHASH, keccak256(bytes("SovereignLexGuard")), keccak256(bytes("1.0")), block.chainid, address(this)));
        bytes32 digest = keccak256(abi.encodePacked("\x19\x01", domainSeparator, structHash));

        address signer = recoverSigner(digest, proof.signature);
        require(signer == sovereignAuditor, "LexGuard: Invalid cryptographic signature");
        return true;
    }

    function isJurisdictionCompliant(address targetContract, bytes4 functionSelector) external view override returns (bool) {
        return !frozenActions[targetContract][functionSelector];
    }

    function setCourtInjunctionFreeze(address targetContract, bytes4 functionSelector, bool freezeState) external onlyAuditor {
        frozenActions[targetContract][functionSelector] = freezeState;
    }

    function recoverSigner(bytes32 _ethSignedMessageHash, bytes memory _sig) internal pure returns (address) {
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(_sig);
        return ecrecover(_ethSignedMessageHash, v, r, s);
    }

    function splitSignature(bytes memory sig) internal pure returns (bytes32 r, bytes32 s, uint8 v) {
        require(sig.length == 65, "invalid signature length");
        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }
    }
}
