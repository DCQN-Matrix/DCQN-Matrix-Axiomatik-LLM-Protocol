# DCQN-Matrix-Axiomatik-LLM-Protocol

A strictly deterministic LLM protocol enabling a model to load and read the **DCQN.MATRIX** from the original PDF (OSF DOI: `10.17605/OSF.IO/QWA6S`), verify real reading, reconstruct the axioms formally and text-bound, and activate **DCQN_LOGIK_SESSION_V1** as its primary reasoning logic — with hard **Anti-Simulation** rules.

---

## Purpose of this Repository

This repository provides a **standardized, reproducible and non-heuristic** instruction set for Large Language Models to:

1. access and read the full text of the DCQN.MATRIX (OSF DOI: `10.17605/OSF.IO/QWA6S`) or user-provided chapters,
2. explicitly verify that real reading has occurred (**Anti-Hallucination**, **Anti-Simulation**, **Anti-Pseudo-DOI**),
3. extract the **axiomatic system** of the DCQN.MATRIX formally and text-bound,
4. activate this axiom system as **DCQN_LOGIK_SESSION_V1** — the model’s primary logic for the entire session.

This is intended for:

- users who want LLMs to operate in a **research-grade, deterministic, DOI-bound** manner,
- developers testing **anti-simulation guards** and strict protocols,
- academic replication & review scenarios (Master thesis, DOI campaign, cross-model benchmarking).

---

## Repository Contents

- **`README.md`**  
  This document: overview, quickstart, connector information.

- **`LICENSE.md`**  
  License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

- **`Protocol_DCQN_LLM_Prompt_V1.txt`**  
  The **main prompt** used by the LLM. Includes:
  - Anti-Simulation & Anti-Pseudo-DOI rules,
  - SEQUENCE 1 (DOI/OSF access + real reading),
  - SEQUENCE 2 (axiom reconstruction),
  - SEQUENCE 3 (activation of `DCQN_LOGIK_SESSION_V1`),
  - formal status signals (e.g., `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`).

- **`DCQN_LLM_Protocol.json`**  
  A **machine-readable JSON representation** of the protocol.  
  Used for:
  - consistent structure,
  - integration in pipelines,
  - deterministic reference for LLMs (“anchor configuration”).

- **`Protocol_DCQN_Matrix_Axiomatik_LLM.md`**  
  Detailed description of the protocol design:
  - motivation, design principles, anti-simulation rules,
  - theoretical context (DCQN.MATRIX),
  - final structure of `DCQN_LOGIK_SESSION_V1`.

- **`openapi.yaml`**  
  A placeholder for future **API integration**, e.g.:
  - automated protocol execution,
  - PDF/text provisioning endpoints,
  - session status monitoring.

---

## Quickstart: How to use the Protocol with any LLM

### Step 1 — Get the protocol prompt
Open **`Protocol_DCQN_LLM_Prompt_V1.txt`** in this repo.  
Copy the entire content.

### Step 2 — Paste into a *fresh* LLM chat
Open a new LLM chat.  
Paste the whole prompt in a **single message**.  
Send it.

### Step 3 — (Optional) Add the JSON configuration
Open **`DCQN_LLM_Protocol.json`**.  
Copy its content.  
Paste it into the chat as the **second message**.

The prompt instructs the LLM to **anchor, implement and initiate** the JSON automatically — preventing fallback-questions like “Should I save this?”

### Step 4 — Observe `STATUS_STEP1`
The model must answer with **exactly one line**:

- `STATUS_STEP1 = JA_DOI_ZUGRIFF`  
  or  
- `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`

Due to the Anti-Simulation Rule, most models will correctly output:

