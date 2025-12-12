<p align="center">
  <img src="https://raw.githubusercontent.com/DCQN-Matrix/DCQN-Matrix-Axiomatik-LLM-Protocol/main/banner.svg"
       alt="DCQN-MATRIX – Deterministic Axiomatics Protocol for LLMs"
       width="100%">
</p>

<h2 align="center">DCQN.MATRIX - Deterministic Axiomatics Protocol for LLMs</h2>

<p align="center">
  Real-text verification • anti-hallucination enforcement • Reproducible LLM reasoning
</p>

<p align="center">
  <a href="https://osf.io/qwa6s"><img src="https://img.shields.io/badge/Project_DOI-10.17605%2FOSF.IO%2FQWA6S-blue"></a>
  <a href="https://doi.org/10.17605/OSF.IO/WZ6AR"><img src="https://img.shields.io/badge/Registration_DOI-10.17605%2FOSF.IO%2FWZ6AR-purple"></a>
  <img src="https://img.shields.io/badge/Protocol-Deterministic-orange">
  <img src="https://img.shields.io/badge/LLM-Evaluation-green">
  <img src="https://img.shields.io/badge/State-Machine_Logic-black">
</p>

---
# **DCQN.Matrix - LLM Protocol**

## Introduction

This repository defines a protocol for the **controlled integration of probabilistic large language models (LLMs)** into a system architecture that adheres to the DCQN Matrix axiomatic framework.

The purpose of this project is to establish a **clear, technically sound interface** between LLMs and deterministic logic layers. It is designed to guide how LLMs should be used where appropriate and **not used where determinism, neutrality, or stability guarantees are required**.

## Motivation

Large language models are inherently probabilistic. Directly relying on them for critical decision-making, neutral evaluation, or stable prioritization introduces risk of inconsistency and unintended generation artifacts. This protocol therefore limits the role of LLMs to **well-defined, non-decisional tasks**.

## Scope and Role

### Purpose

The DCQN LLM Protocol outlines how an LLM can be used:

* to **extract structured information** from context,
* and to **formulate language** for output based on externally approved content.

### Permitted LLM Roles

Within this protocol, an LLM may be used for:

* **READER** reading and interpreting provided content,
* **EXTRACTOR** structured extraction of information,
* **FORMULATOR** language generation for content already approved or authorized by deterministic processes.

LLMs **must not** be used for:

* making decisions that affect system outcomes,
* operational prioritization,
* stability assessments,
* neutrality evaluations.

Those responsibilities are explicitly assigned to **external, deterministic modules**.

## Architecture Overview

This protocol assumes the following high-level architecture:

1. **Deterministic Core**
   External modules responsible for stability, neutrality, decision logic, and priority handling.

2. **LLM Integration Layer**
   A controlled interface where LLMs can receive input and return structured, context-bounded language outputs.

3. **Gate Mechanisms**
   Policy and validation gates that ensure outputs are permissible before passing results downstream.

## Principles

* **Determinism First:** All system-relevant decisions must be resolved outside the LLM.
* **Role Isolation:** An LLM’s function is limited to text handling within a bounded context.
* **Non-decisional LLM Usage:** The protocol explicitly prevents LLM outputs from triggering system state changes.
* **Auditability:** All LLM interactions must be loggable and reviewable without ambiguity.

## Use Cases

The DCQN LLM Protocol is suitable for:

* Extracting structured data from unstructured inputs,
* Generating descriptive text from verified templates,
* Translating or formatting content where logical approval is external.

It is **not** suitable for:

* autonomous reasoning,
* moral or policy judgments,
* stable state determination.

## Compliance and Integration

To integrate within a DCQN-compliant system:

1. Wrap LLM calls with appropriate input sanitization.
2. Apply deterministic gates before and after LLM invocation.
3. Disallow LLM involvement in core decision flows.

## Contributing

Contributions are welcome but must adhere strictly to the protocol’s boundaries:

* No modification that enables LLM decision authority.
* All changes must preserve auditability and determinism.
* Documentation must reflect the role constraints precisely.

## License

This project is open source and may be used under the terms specified in the accompanying LICENSE file.

