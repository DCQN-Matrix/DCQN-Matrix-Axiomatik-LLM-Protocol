# STATUS_DEFINITION.md — Canonical DCQN Machine-State Flags (SSOT-Final)

The following signals are the ONLY valid machine-state identifiers:

STATUS_STEP1 = JA_DOI_ZUGRIFF  
STATUS_STEP1 = NEIN_DOI_ZUGRIFF  
STATUS_STEP2 = JA_VOLLTEXT_GELESEN  
STATUS_STEP2 = NEIN_VOLLTEXT_UNVOLLSTÄNDIG  
DCQN_AXIOMATIK_AKTIV  

Each signal must:

- appear alone on its own line  
- never be translated  
- never be modified  
- never be combined with explanatory text  

Their meaning and rules are governed exclusively by  
Protocol_DCQN_Matrix_Axiomatik_LLM.md (SSOT-Final).
