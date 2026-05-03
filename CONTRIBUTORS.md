# OPRC Contributor Guide

Thank you for joining the **Open Physics Research Collective**. We operate as a meritocratic decentralized collective where technical rigor and open-source principles are the only requirements for advancement[cite: 1, 5].

## 🚦 Technical Standards for Clusters

To ensure the "Containerization Requirement" (Article 3.3.1) is met, all technical contributions must follow these domain-specific standards[cite: 3]:

### 1. High-Energy & Particle (HEPP)
- **Code:** Python (PyROOT, Scikit-hep) or C++.
- **Validation:** Must include config files for event generators (Pythia8/MadGraph).
- **Reproducibility:** Analysis must be runnable via a provided Dockerfile[cite: 3].

### 2. Quantum Systems
- **Circuits:** Provided in OpenQASM 3.0 or Qiskit/Cirq scripts[cite: 2].
- **Verification:** Hybrid variational solvers must include classical benchmarking data[cite: 2].

### 3. Theory & Math
- **Format:** All derivations must be in LaTeX using the standard OPRC class file[cite: 1].
- **Proofs:** Symbolic math scripts (Mathematica/SymPy) are highly encouraged for verification[cite: 2].

---

## 🛠 Contribution Workflow

We utilize the **Request for Comments (RFC)** model for all major research changes[cite: 2]:

1. **The Abstract (RFC Phase):**
   - Open an Issue using the `RFC_TEMPLATE`.
   - Describe the physical phenomenon under study and the proposed methodology[cite: 2].
   - Wait for "Rough Consensus" from at least two Maintainers[cite: 2].

2. **The Active Phase (Pull Request):**
   - Fork the repository and create a feature branch.
   - Submit your code/derivation. 
   - Every commit must be cryptographically signed (GPG) to satisfy Article 10.1.1[cite: 1].

3. **Peer Review:**
   - Reviewers will provide signed, public feedback[cite: 2].
   - Address all blocking technical objections to reach final consensus[cite: 2].

---

## 🎖 Recognition (Contributor Tiers)

The OPRC tracks contributions through the **CRediT** taxonomy[cite: 4]:
- **Level 1 (Observer):** Engages in RFC discussions.
- **Level 2 (Contributor):** Has at least one merged PR in a research cluster[cite: 5].
- **Level 3 (Maintainer):** Vested with the authority to merge RFCs and manage cluster repositories[cite: 5].

*Every contributor must include their ORCID ID in the `CONTRIBUTORS.md` registry to ensure proper academic attribution[cite: 4].*
