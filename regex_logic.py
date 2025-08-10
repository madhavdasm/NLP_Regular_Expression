import re

def extract_domain_name(url):
    pattern = r"https?://(?:www\.)?([A-Za-z0-9-]+)"
    match = re.match(pattern, url)
    
    if match:
        domain = match.group(1)
        return domain, pattern
    else:
        return None, pattern
