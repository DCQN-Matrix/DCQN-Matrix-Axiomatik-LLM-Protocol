# DCQN.MATRIX — Deterministic Evaluation Demo

This folder provides a minimal, reproducible demonstration of how the DCQN Axiomatics Protocol evaluates an LLM.

The demo shows:
- how a model receives a DCQN-compliant prompt,
- how machine-state flags are emitted,
- how axiom extraction works,
- how deterministic behavior is enforced.

## Files

**example_prompt.txt**  
The exact input prompt used for the demonstration.

**example_llm_output.txt**  
The expected deterministic output of a compliant model.

**demo_evaluate.py**  
A small Python script that loads the example prompt and output, compares structure, and verifies deterministic conformance.

**demo_notebook.ipynb**  
A Jupyter notebook containing an interactive walkthrough of the evaluation logic.

## Usage

Run the evaluation script:

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
