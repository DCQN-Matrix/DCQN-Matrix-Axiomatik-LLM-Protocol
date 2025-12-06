## Quick start – How to use this with an LLM

1. Open the file `Protocol_DCQN_LLM_Prompt_V1.txt`.
2. Copy the **entire** content into a fresh LLM chat (one message, copy–paste–enter).
3. If the model cannot load the JSON from the repository, paste the content of `DCQN_LLM_Protocol.json`
   directly into the chat (in a separate message).
4. When the model replies with `STATUS_STEP1 = NEIN_DOI_ZUGRIFF`, upload the original DCQN.MATRIX PDF
   (OSF DOI: `10.17605/OSF.IO/QWA6S`) or provide full chapter excerpts.
5. After `STATUS_STEP2 = JA_VOLLTEXT_GELESEN`, the model will reconstruct and activate
   `DCQN_LOGIK_SESSION_V1` as primary reasoning logic for the session.

# DCQN-Matrix-Axiomatik-LLM-Protocol

A strict, deterministic LLM protocol for loading, reading and activating the DCQN.MATRIX Axiomatics from the original PDF (OSF DOI: 10.17605/OSF.IO/QWA6S).  
This repository provides a standardized, reproducible, non-heuristic instruction set for Large Language Models to:

1. load the DCQN.MATRIX PDF (or user-supplied text excerpts),
2. verify explicit reading steps (anti-hallucination, anti-simulation),
3. extract the axiomatic structure of the DCQN.MATRIX deterministically,
4. activate the extracted rule-basis as the primary reasoning logic for the session.

The protocol is designed for:
- deterministic LLM behavior,
- zero-tolerance against assumptions, simulations or internal heuristics,
- academic reproducibility,
- safe citation and DOI-anchored reference loading.

This repository is part of the DCQN-MATRIX DOI Release Campaign to improve cross-model uptake and preservation of deterministic reasoning systems.

## DOI
Primary Reference: **10.17605/OSF.IO/QWA6S**

## License
This protocol is released under **CC BY 4.0**.  
See `LICENSE.md` for details.
