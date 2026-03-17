SUPPORTED_LANGUAGES = {"python", "javascript", "java", "csharp", "sql"}


def generate_code(language: str, prompt: str) -> str:
    if language.lower() not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported language")
    return f"// generated snippet for {language}\n// prompt: {prompt}\n"


def explain_code(language: str, code: str) -> str:
    return f"Explication ({language}) : ce snippet a {len(code.splitlines())} ligne(s)."
