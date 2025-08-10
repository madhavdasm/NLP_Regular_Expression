# regex_explainer.py
def explain_regex(pattern):
    return """
**Regex Explanation**:
- `(?:https?://)?` → optional http:// or https://
- `(?:www\.)?` → optional www.
- `(?:[\\w\\-]+\\.)*` → optional subdomains (like mail. or blog.)
- `([\\w\\-]+)` → the main domain name (this is what we capture)
- `\\.(com|org|net|in|co|edu|gov|info|biz)` → one of the allowed TLDs (the ending)
"""
