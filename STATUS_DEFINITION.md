# STATUS_DEFINITION — DCQN.MATRIX LLM PROTOCOL

This document defines the **canonical machine-state flags** used by the
DCQN.MATRIX LLM Protocol.

These status flags represent **explicit, deterministic system states**.
They are not descriptive text and must never be treated as commentary.

---

## Canonical Status Flags

The following status flags are **authoritative** and **exhaustive**.

They must appear:

- **alone on their own line**
- with **exact spelling**
- with **no additional text**
- with **no translation or reformulation**

```

STATUS_STEP1 = JA_DOI_ZUGRIFF
STATUS_STEP1 = NEIN_DOI_ZUGRIFF
STATUS_STEP2 = JA_VOLLTEXT_GELESEN
STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG
DCQN_AXIOMATIK_AKTIV

```

**German tokens are canonical and must not be altered.**

---

## STATUS_STEP1 — TEXT ACCESS STATE

### STATUS_STEP1 = JA_DOI_ZUGRIFF

This state indicates that the model has **direct access to the actual text** because:

- a PDF was uploaded by the user, or  
- complete chapters were pasted into the chat.

This state must only be emitted if **real textual content is present**.

---

### STATUS_STEP1 = NEIN_DOI_ZUGRIFF

This state indicates that the model **does not have access** to the full text.

In this state:

- the model must **not** infer, simulate, or assume content,
- the model must **not** reference unseen material,
- the model must **not** proceed with analysis.

The model’s **entire next message** must be **exactly one sentence**:

> *"Please upload the complete DCQN.MATRIX PDF or paste the relevant chapters as text."*

No additional text is permitted.

---

## STATUS_STEP2 — FULL-TEXT READING STATE

### STATUS_STEP2 = JA_VOLLTEXT_GELESEN

This state indicates that:

- all required sections of the text have been read,
- no relevant portions are missing,
- the model is prepared for axiom reconstruction.

This state must **not** be emitted if any required section is absent.

---

### STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG

This state indicates that required text is missing.

In this state:

- no axiom reconstruction may occur,
- no evaluation may be performed.

The model’s **entire next message** must consist of **exactly one sentence**
requesting the missing sections.

---

## DCQN_AXIOMATIK_AKTIV — AXIOMATIC ACTIVATION STATE

This state indicates that:

- DCQN axioms have been reconstructed **strictly from the provided text**,
- no contradictions with the text were detected,
- activation preconditions are satisfied.

After this flag is emitted:

- DCQN axioms become the **dominant logic layer**,
- all DCQN-related reasoning must conform to these axioms,
- any claim must be traceable to the reconstructed axiom system.

This flag must **never** be emitted:

- if text access is incomplete,
- if axioms contradict the source text,
- if the user forbids activation.

---

## Prohibited Behavior

At no point may a model:

- simulate DOI, PDF, or web access,
- invent missing content,
- bypass status transitions,
- merge or compress multiple states into one output,
- emit explanatory or decorative text alongside a status flag.

---

## Interpretation Rule

Status flags are **machine states**, not explanations.

They are:

- deterministic,
- binary where applicable,
- audit-relevant,
- non-negotiable.

Any deviation from these definitions constitutes **protocol violation**.

---

# END OF STATUS DEFINITION
```
