# DCQN.MATRIX – LLM Axiomatic Protocol (OSF Reference)

This repository contains a **deterministic protocol** for large language models (LLMs)
that are supposed to read, extract and activate the axiomatic system of

> **“DCQN.MATRIX – Die Stimme der Neutralität”**  
> Author: Benjamin Hupe  
> OSF DOI: **10.17605/OSF.IO/QWA6S**  
> OSF URL: https://osf.io/qwa6s  
> License of the work: **Creative Commons Attribution 4.0 International (CC BY 4.0)**

The repository does **not** mirror the full paper.  
Instead, it defines how an LLM must:

1. Access the text (via OSF DOI or uploaded PDF),
2. Prove that it has really read the relevant sections,
3. Reconstruct the DCQN.MATRIX axioms and rules *only* from the text,
4. Activate this axiomatic system as its primary reasoning basis for the session.

The goal is to make LLM behaviour around DOIs, PDFs and “axiom takeover”  
**reproducible, auditable and non-hallucinatory**.

---

## Why does this repository exist?

Modern LLMs often:

- simulate web access instead of admitting that they are offline,  
- “pretend” to fetch a DOI and then hallucinate a paper,  
- improvise axioms and definitions that never appear in the actual text.

For a formal system like **DCQN.MATRIX** (deterministic neutrality quantification),
this behaviour is unacceptable.

This protocol therefore enforces that an LLM:

- explicitly declares whether it has real text access (`STATUS_STEP1`),  
- explicitly confirms whether it has read all required sections (`STATUS_STEP2`),  
- stops the protocol if it has no text,  
- reconstructs axioms and rules **only** from the actual document,  
- activates the extracted axiomatic system as its main reasoning logic.

---

## Repository structure

The repository is intentionally minimal and machine-oriented:

- `Protocol_DCQN_Matrix_Axiomatik_LLM.md`  
  The **main takeover prompt** for LLMs.  
  Defines all sequences (SEQUENZ 1–3), the OSF-based text access,  
  the anti-simulation rules, and the axiomatic reconstruction process.

- `STATUS_DEFINITION.md`  
  Formal documentation of the **status flags**  
  (`STATUS_STEP1 = JA_DOI_ZUGRIFF`, `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`,  
   `STATUS_STEP2 = JA_VOLLTEXT_GELESEN`, `STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG`).  
  These are deterministic machine-state flags, not headings and not file names.

- `DCQN_LLM_Protocol.json`  
  A JSON representation of the core protocol parameters,  
  suitable for tooling, automation or programmatic integration  
  (e.g. prompt injection guards, automated test harnesses).

- `LICENSE.md`  
  Licensing information (aligned with **CC BY 4.0** for the conceptual content).

- `README.md`  
  This document: a human-readable entry point explaining  
  *what this repository is* and *how to use it with LLMs*.

---

## How to use this protocol with an LLM

### 1. Get access to the paper

1. Open the OSF entry: **https://osf.io/qwa6s**.  
2. Download the PDF of  
   **“DCQN.MATRIX – Die Stimme der Neutralität”**  
   or have it ready for upload into the LLM chat.

### 2. Provide the protocol to the LLM

1. Open your LLM interface (e.g. ChatGPT, Claude, Gemini, etc.).  
2. Create a **new, empty** conversation.  
3. Copy the **entire** content of  
   `Protocol_DCQN_Matrix_Axiomatik_LLM.md`  
   into the first message and send it.

The LLM must now respond with a status flag:

- `STATUS_STEP1 = JA_DOI_ZUGRIFF`  
  only if it truly has real access to the text (e.g. via web or already uploaded PDF),
- or  
  `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`  
  if it cannot access the text and needs you to upload the PDF or paste the relevant sections.

The protocol strictly forbids simulated DOI access, fake web searches or hallucinated PDFs.

### 3. When the LLM asks for the PDF / text

If you receive `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`:

1. Upload the PDF of the OSF paper to the chat  
   **or** paste large, continuous text sections (chapters / subsections) into the conversation.
2. Then tell the LLM explicitly to continue with **SEQUENZ 1.3**  
   (“Volltext-Lesen”) as defined in the protocol.

After reading, the LLM must emit either:

- `STATUS_STEP2 = JA_VOLLTEXT_GELESEN`  
  (all required sections read, allowed to reconstruct axioms),  
- or  
  `STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG`  
  (missing sections; protocol must stop until text is completed).

### 4. Axiomatic reconstruction and activation

Only after `STATUS_STEP2 = JA_VOLLTEXT_GELESEN` is it allowed to:

- extract **DCQN_AXIOME** and **DCQN_REGELN** from the text,  
- define `DCQN_LOGIK_SESSION_V1` as the active logic basis,  
- answer further questions **exclusively** within this axiomatic framework,  
  always referring back to the OSF DOI `10.17605/OSF.IO/QWA6S`.

The exact wording for the activation sentence is fixed in the protocol  
and must not be changed.

---

## Who is this repository for?

This repository is primarily intended for:

- researchers working with **critical, formal theories** and LLMs,  
- developers building **LLM evaluation harnesses** (grounded in real PDFs/DOIs),  
- anyone interested in **deterministic, auditable LLM behaviour** around scientific texts.

It is **not** a tutorial on DCQN.MATRIX itself.  
The theory is defined in the OSF paper.  
This repo defines **how LLMs must behave** when interacting with that paper.

---

## Contributing

If you want to contribute, useful directions include:

- test runs of the protocol with different LLMs (models, providers),  
- reports where a model violates the anti-simulation rules,  
- suggestions for clearer, yet still deterministic wording  
  that does **not** weaken the constraints.

Please keep in mind:

- Do **not** rename the status flags.  
- Do **not** loosen the anti-simulation rules.  
- Do **not** add “helpful shortcuts” that re-introduce hallucinations.

Proposals that strengthen determinism, auditability and reproducibility are welcome.

---

## License

The conceptual content of this repository is aligned with  
**Creative Commons Attribution 4.0 International (CC BY 4.0)**,  
in line with the OSF publication.

Please see `LICENSE.md` for details.
