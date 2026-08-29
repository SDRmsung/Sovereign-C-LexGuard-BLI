# -*- coding: utf-8 -*-
"""
Sovereign LexGuard - Formal SAT Constraint Solver
Based on Pure Python DPLL (Davis-Putnam-Logemann-Loveland) Algorithm.
Guarantees mathematical satisfiability and detects legal clause contradictions.
"""
from typing import List, Dict, Tuple, Optional, Set

class SATSolver:
    @staticmethod
    def solve(num_vars: int, clauses: List[List[int]]) -> Tuple[bool, Optional[Dict[int, bool]], Optional[List[List[int]]]]:
        """
        Solves a boolean formula in Conjunctive Normal Form (CNF).
        Returns: (is_satisfiable, satisfying_assignment, conflicting_clauses)
        """
        def unit_propagate(cls: List[List[int]], assignment: Dict[int, bool]):
            changed = True
            while changed:
                changed = False
                for c in cls:
                    unassigned = [lit for lit in c if abs(lit) not in assignment]
                    satisfied = any((lit > 0 and assignment.get(lit) is True) or 
                                    (lit < 0 and assignment.get(-lit) is False) for lit in c)
                    if satisfied:
                        continue
                    if len(unassigned) == 0:
                        return False, cls # Conflict
                    if len(unassigned) == 1:
                        unit_lit = unassigned[0]
                        var = abs(unit_lit)
                        val = unit_lit > 0
                        assignment[var] = val
                        changed = True
            return True, cls

        def dpll(cls: List[List[int]], assignment: Dict[int, bool]):
            success, _ = unit_propagate(cls, assignment)
            if not success:
                return False, None

            # Check if all clauses satisfied
            all_sat = True
            for c in cls:
                if not any((lit > 0 and assignment.get(lit) is True) or 
                           (lit < 0 and assignment.get(-lit) is False) for lit in c):
                    all_sat = False
                    break
            if all_sat:
                return True, assignment

            # Choose unassigned variable
            unassigned_vars = [v for v in range(1, num_vars + 1) if v not in assignment]
            if not unassigned_vars:
                return True, assignment
            var = unassigned_vars[0]

            # Try True
            assign_true = assignment.copy()
            assign_true[var] = True
            sat, res = dpll(cls, assign_true)
            if sat:
                return True, res

            # Try False
            assign_false = assignment.copy()
            assign_false[var] = False
            return dpll(cls, assign_false)

        initial_assignment = {}
        is_sat, final_model = dpll(clauses, initial_assignment)
        if is_sat:
            return True, final_model, None
        else:
            return False, None, clauses
