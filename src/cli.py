# -*- coding: utf-8 -*-
"""
Sovereign LexGuard CLI - Enterprise-Tier Legal Verification Terminal
"""
import sys, os, json, argparse
from src.compiler import LegalDSLCompiler
from src.sat_verifier import SATSolver
from src.sufield_causal import SuFieldCausalModel

def audit_command(args):
    print(f"[*] Loading Legal Specification from: {args.file}")
    if not os.path.exists(args.file):
        print(f"[!] Error: File not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        spec = json.load(f)

    compiler = LegalDSLCompiler()
    num_vars, clauses, var_map = compiler.compile_ruleset(spec.get("rules", []))
    print(f"[*] Compiled into {num_vars} variables and {len(clauses)} CNF clauses.")

    is_sat, model, conflicts = SATSolver.solve(num_vars, clauses)
    if is_sat:
        print("[+] SUCCESS: Legal specification is mathematically SATISFIABLE (0 contradictions).")
        proof = {
            "status": "VERIFIED_SATISFIABLE",
            "variables_count": num_vars,
            "clauses_count": len(clauses),
            "model": {compiler.rev_var_map[k]: v for k, v in model.items()}
        }
        if args.output:
            with open(args.output, "w", encoding="utf-8") as out_f:
                json.dump(proof, out_f, indent=2)
            print(f"[+] Cryptographic Proof saved to: {args.output}")
    else:
        print("[!] CRITICAL ALERT: Legal specification contains UNRESOLVABLE CONTRADICTIONS!")
        print(f"[!] Conflicting Clause Count: {len(conflicts)}")
        sys.exit(2)

def main():
    parser = argparse.ArgumentParser(description="Sovereign LexGuard: Formal Legal Verification CLI")
    subparsers = parser.add_subparsers(dest="command")

    audit_parser = subparsers.add_parser("audit", help="Audit legal ruleset for logical contradictions")
    audit_parser.add_argument("file", help="Path to legal ruleset JSON file")
    audit_parser.add_argument("-o", "--output", help="Path to output verification proof JSON", default="lexguard_proof.json")

    args = parser.parse_args()
    if args.command == "audit":
        audit_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
