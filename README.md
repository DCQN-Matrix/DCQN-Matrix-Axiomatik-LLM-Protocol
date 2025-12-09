<p align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg"
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs"
       width="100%">
</p>

<h2 align="center">DCQN-MATRIX — Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  Real-text verification • Zero hallucination • Reproducible LLM reasoning
</p>

<p align="center">
  <a href="https://osf.io/qwa6s"><img src="https://img.shields.io/badge/Project_DOI-10.17605%2FOSF.IO%2FQWA6S-blue"></a>
  <a href="https://doi.org/10.17605/OSF.IO/WZ6AR"><img src="https://img.shields.io/badge/Registration_DOI-10.17605%2FOSF.IO%2FWZ6AR-purple"></a>
  <img src="https://img.shields.io/badge/Protocol-Deterministic-orange">
  <img src="https://img.shields.io/badge/LLM-Evaluation-green">
  <img src="https://img.shields.io/badge/State-Machine_Logic-black">
</p>

---

# DCQN.MATRIX – LLM Axiomatic Protocol (OSF Reference)

This repository defines a deterministic, reproducible, DOI-anchored protocol enabling LLMs to:

1. verify access to the PDF  
2. read required scientific sections  
3. reconstruct axioms and rules  
4. activate the axiomatic system as the session’s primary logic layer  

The protocol prevents:

- simulated DOI access  
- hallucinated PDF content  
- heuristic or interpolated inference  
- uncontrolled reasoning drift  

---

## Repository structure

- Protocol_DCQN_Matrix_Axiomatik_LLM.md  
- STATUS_DEFINITION.md  
- DCQN_LLM_Protocol.json  
- openapi.yaml  
- LICENSE.md  
- README.md  

---

## Workflow

1. User downloads PDF from https://osf.io/qwa6s  
2. User opens a fresh LLM chat  
3. User pastes the protocol  
4. Model emits `STATUS_STEP1`  
5. User uploads PDF if needed  
6. Model reads text → emits `STATUS_STEP2`  
7. Model reconstructs axioms  
8. Model activates → `DCQN_AXIOMATIK_AKTIV`  

This ensures deterministic, fully auditable scientific reasoning.

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)
