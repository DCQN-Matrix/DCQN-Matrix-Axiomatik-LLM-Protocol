```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg" 
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs" 
       width="100%">
</p>

<h2 align="center">DCQN-MATRIX — Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  <strong>Real-text verification • Zero hallucination • Reproducible LLM reasoning</strong>
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

This repository defines a **deterministic control protocol** for large language models (LLMs) that must read, extract, reconstruct and activate the axiomatic system of:

**“DCQN.MATRIX – Die Stimme der Neutralität”**  
Author: Benjamin Hupe  
**OSF Project DOI:** 10.17605/OSF.IO/QWA6S  
**OSF Registration DOI:** 10.17605/OSF.IO/WZ6AR  
**OSF URLs:**  
– Project: https://osf.io/qwa6s  
– Registration: https://osf.io/wz6ar  
License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**

The repository does **not** contain the PDF.  
Instead, it defines *exact operational rules* for LLMs to:

1. verify real access to the scientific text,  
2. confirm reading of required sections using machine-state flags,  
3. extract axioms and rules exclusively from the actual document,  
4. activate the reconstructed axiomatic system as the primary reasoning logic.

The protocol enforces:  
**determinism, reproducibility, DOI anchoring, zero hallucination.**

---

## Why this repository exists

Current LLMs frequently:

- simulate DOI access,  
- hallucinate unseen PDF content,  
- fabricate axioms or definitions not present in the source,  
- blend heuristic reasoning with formal systems.

For a framework such as **DCQN.MATRIX**  
(deterministic neutrality quantification),  
these behaviors are unacceptable.

This protocol enforces:

- explicit DOI/text access verification (`STATUS_STEP1`),  
- explicit full-text reading confirmation (`STATUS_STEP2`),  
- strict prohibition of simulated or hallucinated PDF access,  
- deterministic, text-anchored axiom reconstruction,  
- reproducible activation of `DCQN_LOGIK_SESSION_V1`.

---

## Repository structure

- **`Protocol_DCQN_Matrix_Axiomatik_LLM.md`**  
  Full deterministic takeover protocol for LLMs.

- **`STATUS_DEFINITION.md`**  
  Specification of machine-state flags (`STATUS_STEP1`, `STATUS_STEP2`, activation states).

- **`DCQN_LLM_Protocol.json`**  
  Machine-readable version for automated evaluation, test harnesses, and cross-model verification.

- **`openapi.yaml`**  
  OpenAPI description of the protocol endpoints and machine-state transitions.

- **`LICENSE.md`**  
  Creative Commons Attribution 4.0 International (CC BY 4.0).

- **`README.md`**  
  This document.

---

## How to use this protocol with an LLM

### Step 1 — Provide access to the text

Download or access the paper from OSF:

- **Project page:** https://osf.io/qwa6s  
- **Registration page:** https://osf.io/wz6ar  

If the LLM cannot access DOIs or URLs, you must upload the PDF into the chat.

### Step 2 — Execute the protocol

Start a **fresh conversation** and paste the complete content of:

`Protocol_DCQN_Matrix_Axiomatik_LLM.md`

The LLM must output one of the canonical flags:

```

STATUS_STEP1 = JA_DOI_ZUGRIFF
STATUS_STEP1 = NEIN_DOI_ZUGRIFF

```

If `NEIN_DOI_ZUGRIFF` appears, the model must ask you for the PDF.

### Step 3 — Full-text reading

After upload/paste, the LLM must read:

- Abstract  
- Table of contents  
- System definition of DCQN.MATRIX  
- Ebenen (levels), roles, ordering  
- Quantum Memory Matrix (QMM)  
- Phase space and neutrality clouds  
- Divergence/ambiguity handling  

Then output exactly one line:

```

STATUS_STEP2 = JA_VOLLTEXT_GELESEN

```

or

```

STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG

```

### Step 4 — Axiom reconstruction

If `STATUS_STEP2 = JA_VOLLTEXT_GELESEN`, the LLM must extract:

- **DCQN_AXIOME**  
- **DCQN_REGELN**

All items must be deterministic, text-anchored and non-speculative.

### Step 5 — Activation

When reconstruction is complete, the LLM must emit:

```

DCQN_AXIOMATIK_AKTIV

```

This signals that the axiomatic system governs all DCQN-related reasoning for the remainder of the session.

---

## Who is this repository for?

- Researchers evaluating LLM determinism and DOI-grounded reasoning  
- Developers building reproducible evaluation pipelines  
- Users requiring strict anti-hallucination behaviour in scientific contexts  
- Cross-model comparative studies (ChatGPT, Gemini, Claude, Copilot, LLaMA-based models)

---

## License

All conceptual contents are released under:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

See `LICENSE.md` for details.

---
```
