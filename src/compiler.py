# -*- coding: utf-8 -*-
"""
Sovereign LexGuard - Legal-DSL to Formal CNF Compiler
Extracts atomic legal propositions, obligations, rights, and converts them to CNF clauses.
"""
from typing import List, Dict, Any, Tuple
import json

class LegalDSLCompiler:
    def __init__(self):
        self.var_map: Dict[str, int] = {}
        self.rev_var_map: Dict[int, str] = {}
        self.clauses: List[List[int]] = []
        self.clause_descriptions: List[str] = []

    def _get_var(self, proposition: str) -> int:
        clean_prop = proposition.strip().lower()
        if clean_prop not in self.var_map:
            new_id = len(self.var_map) + 1
            self.var_map[clean_prop] = new_id
            self.rev_var_map[new_id] = clean_prop
        return self.var_map[clean_prop]

    def add_implication(self, condition: str, consequence: str, desc: str = ""):
        """Adds rule: condition -> consequence (CNF: not condition or consequence)"""
        cond_id = self._get_var(condition)
        cons_id = self._get_var(consequence)
        self.clauses.append([-cond_id, cons_id])
        self.clause_descriptions.append(desc or f"{condition} => {consequence}")

    def add_prohibition(self, condition: str, forbidden_action: str, desc: str = ""):
        """Adds rule: condition -> not forbidden_action (CNF: not condition or not forbidden_action)"""
        cond_id = self._get_var(condition)
        act_id = self._get_var(forbidden_action)
        self.clauses.append([-cond_id, -act_id])
        self.clause_descriptions.append(desc or f"{condition} => NOT {forbidden_action}")

    def add_mutual_exclusion(self, prop_a: str, prop_b: str, desc: str = ""):
        """Adds rule: not (prop_a and prop_b) (CNF: not prop_a or not prop_b)"""
        id_a = self._get_var(prop_a)
        id_b = self._get_var(prop_b)
        self.clauses.append([-id_a, -id_b])
        self.clause_descriptions.append(desc or f"EXCLUSIVE({prop_a}, {prop_b})")

    def add_mandatory_fact(self, proposition: str, value: bool = True, desc: str = ""):
        """Adds asserted fact: proposition == True/False"""
        var_id = self._get_var(proposition)
        self.clauses.append([var_id if value else -var_id])
        self.clause_descriptions.append(desc or f"ASSERT({proposition} = {value})")

    def compile_ruleset(self, ruleset: List[Dict[str, Any]]) -> Tuple[int, List[List[int]], Dict[str, int]]:
        for r in ruleset:
            r_type = r.get("type", "implication")
            desc = r.get("description", "")
            if r_type == "implication":
                self.add_implication(r["if"], r["then"], desc)
            elif r_type == "prohibition":
                self.add_prohibition(r["if"], r["forbidden"], desc)
            elif r_type == "mutual_exclusion":
                self.add_mutual_exclusion(r["a"], r["b"], desc)
            elif r_type == "assertion":
                self.add_mandatory_fact(r["fact"], r.get("value", True), desc)
        return len(self.var_map), self.clauses, self.var_map
