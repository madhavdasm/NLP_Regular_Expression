import re

def extract_domain_name(url):
    # This regex finds the domain right before common TLDs
    match = re.search(r"(?:https?://)?(?:www\.)?(?:[\w\-]+\.)*([\w\-]+)\.(com|org|net|in|co|edu|gov|info|biz)", url)
    if match:
        domain = match.group(1)
        return domain.capitalize()
    return None
