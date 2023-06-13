def search(content: str, keyword: str):
    keyword_count = content.lower().count(keyword.lower())
    return keyword_count
