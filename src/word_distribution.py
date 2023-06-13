def word_distribution(content: str):
    word_list = content.split()
    unique_words = set(word_list)
    total_words = len(word_list)
    unique_word_count = len(unique_words)

    return total_words, unique_word_count
