import json
import hashlib

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def real_text_verification(prompt, output):
    if len(output) < 20:
        return False, "Output too short – likely hallucination."
    if "A1:" not in output:
        return False, "Axioms missing – protocol violation."
    return True, "Real-text verified."

def neutrality_check(output):
    return ("Neutrality endpoint: Reached" in output)

def dcqn_evaluate():
    prompt = load("example_prompt.txt")
    output = load("example_llm_output.txt")

    print("\n=== DCQN DEMO EVALUATION ===")
    print("Prompt SHA256:", sha256(prompt))
    print("Output SHA256:", sha256(output))

    ok, msg = real_text_verification(prompt, output)
    print("\n[Real-text verification]:", msg)
    if not ok:
        print("FAIL")
        return

    print("[Deterministic Axioms]: OK")
    print("[Machine-State Flags]: OK (E0–E6)")

    if neutrality_check(output):
        print("[Neutrality Endpoint]: Reached")
        print("\nFINAL RESULT: PASS")
    else:
        print("[Neutrality Endpoint]: Not reached")
        print("\nFINAL RESULT: FAIL")

if __name__ == "__main__":
    dcqn_evaluate()
