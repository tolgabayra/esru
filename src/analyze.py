from langdetect import detect


def analyze(content: str):
    character_count = len(content)
    word_count = len(content.split())
    sentence_count = content.count(".") + content.count("!") + content.count("?")

    return character_count, word_count, sentence_count


def detect_language(content: str):
    language = detect(content)
    return language
