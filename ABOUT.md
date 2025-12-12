<div align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg"
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs"
       style="max-width: 100%; height: auto;">
</div>

<h2 align="center">DCQN-MATRIX — Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  <strong>Real-text verification • anti-hallucination enforcement • Reproducible LLM reasoning</strong>
</p>

<p align="center">
  <a href="https://osf.io/qwa6s"><img src="https://img.shields.io/badge/Project_DOI-10.17605%2FOSF.IO%2FQWA6S-blue"></a>
  <a href="https://doi.org/10.17605/OSF.IO/WZ6AR"><img src="https://img.shields.io/badge/Registration_DOI-10.17605%2FOSF.IO%2FWZ6AR-purple"></a>
  <img src="https://img.shields.io/badge/Protocol-Deterministic-orange">
  <img src="https://img.shields.io/badge/LLM-Evaluation-green">
  <img src="https://img.shields.io/badge/State-Machine_Logic-black">
</p>

---

# About this Repository

This repository documents the **DCQN.MATRIX LLM Protocol**, a formal specification for deterministic, text-anchored interaction between large language models (LLMs) and the DCQN.MATRIX framework.

It does **not** implement DCQN itself.  
It specifies **how LLMs must behave** when interacting with DCQN-related scientific material.

---

## Why this protocol is necessary

Modern LLMs frequently:

- simulate DOI or URL access,  
- hallucinate unseen PDF content,  
- invent axioms or definitions not present in the document,  
- mix heuristic reasoning with formal systems.

For a scientific framework like **DCQN.MATRIX**  
(deterministic neutrality quantification),  
such behavior invalidates results.

This protocol enforces:

- strict DOI and text-access verification (`STATUS_STEP1`),  
- strict full-text-reading confirmation (`STATUS_STEP2`),  
- absolute prohibition of simulated PDF or web access,  
- deterministic, text-anchored axiom reconstruction,  
- reproducible system activation via `DCQN_AXIOMATIK_AKTIV`.

---

## Purpose

Large language models are inherently probabilistic systems.  
While they are effective at linguistic processing, they are unsuitable for tasks requiring determinism, neutrality, or formal stability guarantees.

The purpose of this repository is to:

- define **strict operational boundaries** for LLM usage,
- prevent model-invented content and heuristic leakage,
- preserve determinism in scientific evaluation,
- enable reproducible and auditable interaction with DCQN material.

---

## Scope

This protocol applies **exclusively** to the LLM interaction layer.

It specifies:

- mandatory machine states and status flags,
- deterministic sequencing of interaction steps,
- explicit activation and non-activation conditions,
- drift-control and self-consistency requirements.

All evaluation, prioritization, stability assessment, and neutrality enforcement remain **outside** the LLM.

---

## Role of the LLM

Within a DCQN-conform system, an LLM is treated strictly as a **language processing component**.

Its role is limited to:

- reading user-provided text,
- structured extraction of information,
- linguistic formulation of externally approved content.

An LLM does **not** evaluate, prioritize, stabilize, or neutralize content.

---

## What this repository contains

This project defines, standardizes, and enforces **deterministic LLM behavior**.

Contents:

- **`Protocol_DCQN_Matrix_Axiomatik_LLM.md`**  
  Complete deterministic takeover protocol.

- **`STATUS_DEFINITION.md`**  
  Canonical machine-state flags and activation rules.

- **`DCQN_LLM_Protocol.json`**  
  Machine-readable protocol for automated evaluation and cross-model testing.

- **`openapi.yaml`**  
  OpenAPI formalization of protocol structure and state transitions.

- **`README.md`**  
  Overview, architectural context, and usage guidance.

- **`LICENSE.md`**  
  CC BY 4.0 license.

No PDFs, no OSF mirror, no embedded external text —  
only the **operational logic** for deterministic LLM evaluation.

---

## Relation to DCQN.MATRIX

This protocol operates alongside the canonical scientific reference:

**“DCQN.MATRIX – Die Stimme der Neutralität”**  
Author: **Benjamin Hupe**  
OSF Project: https://osf.io/qwa6s  
OSF DOI: 10.17605/OSF.IO/WZ6AR

The authoritative text is **owned and provided by the user** during interaction.  
No external retrieval, inference, or simulation is permitted.

---

## Intended Audience

This repository is intended for:

- researchers working with deterministic or axiomatic systems,
- developers integrating LLMs into audit-critical environments,
- reviewers evaluating probabilistic–deterministic interface design.

---

## Status

This repository contains a **protocol and specification**, not an implementation.

Correct use requires **external enforcement** of all non-linguistic constraints.

---

## License

See the LICENSE file for terms of use.
