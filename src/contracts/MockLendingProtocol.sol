// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

import "./ILexGuard.sol";

contract MockLendingProtocol {
    ILexGuard public immutable lexGuard;
    mapping(address => uint256) public collateral;
    mapping(address => uint256) public debt;

    event Liquidated(address indexed borrower, uint256 amount);

    constructor(address _lexGuard) {
        lexGuard = ILexGuard(_lexGuard);
    }

    function liquidate(address borrower, ILexGuard.RuleProof calldata proof) external {
        // Pre-Execution Compliance Gatekeeper
        bytes32 ruleHash = keccak256(abi.encodePacked("RWA_LIQUIDATION_RULE_V1"));
        require(lexGuard.verifyAndEnforce(ruleHash, proof), "Compliance Gate: Proof rejected");
        require(lexGuard.isJurisdictionCompliant(address(this), msg.sig), "Compliance Gate: Action frozen by court injunction");

        collateral[borrower] = 0;
        debt[borrower] = 0;
        emit Liquidated(borrower, 100);
    }
}
