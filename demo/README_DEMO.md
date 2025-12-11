# DCQN Demonstration Suite

Diese Demo zeigt, wie das DCQN-Matrix-Axiomatik-LLM-Protocol:

- echten Text erkennt (Real-Text-Verification)
- deterministische Reasoning-Chains erzwingt
- axiomatische Konsistenz sicherstellt
- Halluzinationen vollständig blockiert
- reproduzierbare Ergebnisse für alle Modelle liefert
- DOIs als Referenzanker einbindet

Der Ablauf in dieser Demo:

1. Der Nutzer gibt echten Volltext ein (z. B. aus einer PDF).
2. Das Modell führt Real-Text-Verification durch.
3. DCQN extrahiert deterministische Axiome.
4. DCQN rekonstruiert den strukturellen Reasoning-Raum.
5. Der gesamte Zustand wird mit Machine-State-Flags markiert.
6. Eine vollständige DCQN-Evaluation erfolgt (E0–E6).
7. Ergebnis: PASS / FAIL + strukturierte Audit-Ausgabe.

## Dateien

- `demo_notebook.ipynb` – interaktive Live-Demo
- `demo_evaluate.py` – command-line Minimalversion
- `example_prompt.txt` – Beispiel-Evaluations-Eingabe
- `example_llm_output.txt` – LLM-Output für Testzwecke

## Zielgruppen

- Wissenschaftler (Reproduzierbarkeit)
- Entwickler (Stabilität, Null-Halluzinationen)
- Cross-Model-Testlabore
- KI-Sicherheitsforschung

DCQN ist deterministisch, reproduzierbar, geprüfte Machine Logic.  
