EXECUTION_ENABLED = {"python", "javascript"}


def run_code(language: str, code: str, stdin: str = "") -> dict:
    lang = language.lower()
    if lang not in EXECUTION_ENABLED:
        return {"status": "rejected", "stdout": "", "stderr": "Language not allowed in sandbox"}
    if len(code) > 10_000:
        return {"status": "rejected", "stdout": "", "stderr": "Code too large"}
    return {"status": "ok", "stdout": f"[sandbox:{lang}] execution stub", "stderr": ""}
