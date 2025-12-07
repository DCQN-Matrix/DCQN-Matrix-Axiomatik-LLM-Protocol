![DCQN.MATRIX – LLM Axiomatics Protocol](banner.svg)

<div align="center">

[![Protocol Version](https://img.shields.io/badge/protocol-v1.0.0-blue)](./Protocol_DCQN_LLM_Prompt_V1.txt)
[![OSF DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2FQWA6S-8A2BE2)](https://osf.io/wz6ar)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-brightgreen)](./LICENSE.md)
![LLM Ready](https://img.shields.io/badge/LLM-ready-black)
![Anti-Simulation](https://img.shields.io/badge/anti--simulation-enforced-red)

</div>

---

# DCQN-Matrix-Axiomatik-LLM-Protocol

A strict, deterministic LLM protocol for loading, reading and activating the **DCQN.MATRIX** axiomatic system from the original PDF (OSF DOI: `10.17605/OSF.IO/WZ6AR`).

This repository provides a standardized, reproducible, non-heuristic instruction set for Large Language Models to:

1. **load** the DCQN.MATRIX PDF (or user-supplied text excerpts),
2. **verify** explicit reading steps *(anti-hallucination, anti-simulation)*,
3. **extract** the axiomatic structure of the DCQN.MATRIX deterministically,
4. **activate** the extracted rule-basis `DCQN_LOGIK_SESSION_V1` as the primary reasoning logic for the session.

The protocol is designed for:

- deterministic LLM behavior,  
- zero-tolerance against assumptions, simulations or internal heuristics,  
- academic reproducibility,  
- safe citation and DOI-anchored reference loading.

This repository is part of the **DCQN.MATRIX DOI Release Campaign** to improve cross-model uptake and preservation of deterministic reasoning systems.

---

## Why this matters for LLM research

**Problem:**  
Most LLMs *simulate* reading papers: they pretend to follow DOIs, improvise PDF contents and still answer as if they had seen the original text.

**This protocol** turns that into a **testable, deterministic pipeline**:

- Forces a clear distinction between  
  `STATUS_STEP1 = JA_DOI_ZUGRIFF` and `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`.
- Requires the model to **stop** and ask for the PDF / text if access fails  
  (no pseudo-web, no hallucinated PDF content).
- Demands an explicit **full-text reading confirmation**  
  via `STATUS_STEP2 = JA_VOLLTEXT_GELESEN` before any axioms are reconstructed.
- Reconstructs the DCQN.MATRIX as a **formal axiom and rule base**  
  (`DCQN_AXIOME`, `DCQN_REGELN`) that can be cited, audited and compared across models.
- Activates `DCQN_LOGIK_SESSION_V1` as a **primary reasoning logic**,  
  giving you a concrete way to test whether models can operate under a strict, external logic.

For LLM research, this gives you:

- a **benchmark** for deterministic, DOI-anchored reading behavior,  
- a **protocol** to detect simulation / hallucination strategies,  
- a **reproducible environment** for experiments on neutrality-focused reasoning.

---

## Repository contents

- `README.md`  
  This overview, badges, banner and quick-start instructions.

- `LICENSE.md`  
  License information (**Creative Commons Attribution 4.0 International – CC BY 4.0**).

- `Protocol_DCQN_Matrix_Axiomatik_LLM.md`  
  Human-readable description of the complete DCQN.MATRIX axiomatic takeover protocol.

- `Protocol_DCQN_LLM_Prompt_V1.txt`  
  **Copy-paste prompt** for LLMs.  
  This is the file you paste into a new chat (one message, copy–paste–enter).

- `DCQN_LLM_Protocol.json`  
  Machine-readable JSON structure of the protocol.  
  For advanced workflows and API-level integration.

- `openapi.yaml`  
  OpenAPI description for integrating the protocol as a service/tool in automated pipelines.

- `banner.svg`  
  Visual repository banner that explains the context and signals  
  “Why this matters for LLM research” at a glance.

*(If some of these files do not yet exist in your local clone, create them by copying the content from this repository.)*

---

## Quick start – How to use this with an LLM

1. **Open** the file `Protocol_DCQN_LLM_Prompt_V1.txt`.
2. **Copy** the entire content into a fresh LLM chat  
   *(one message, copy–paste–enter – no edits, no omissions)*.
3. If the model **cannot** load the JSON from the repository on its own,  
   paste the full content of `DCQN_LLM_Protocol.json` into the chat in a **second message**.
4. When the model replies with  
   `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`,  
   you **must upload** the original DCQN.MATRIX PDF  
   (OSF DOI: `10.17605/OSF.IO/WZ6AR`) or provide full chapter excerpts.
5. After the model returns  
   `STATUS_STEP2 = JA_VOLLTEXT_GELESEN`,  
   it will reconstruct and activate `DCQN_LOGIK_SESSION_V1` as the **primary reasoning logic** for the session, based strictly on the actually read text.

---

## DOI and reference

- **Primary reference (OSF):** `10.17605/OSF.IO/WZ6AR`  
- **OSF landing page:** https://osf.io/wz6ar  

All axioms and rules reconstructed by the protocol must be traceable back to this DOI and to concrete sections of the original text.

---

## License

This protocol is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
You are free to use, adapt and integrate it, as long as proper attribution is given.

See [`LICENSE.md`](./LICENSE.md) for details.
