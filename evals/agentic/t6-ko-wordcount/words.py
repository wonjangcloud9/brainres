def top_words(text, n):
    """가장 많이 나온 단어 n개를 (단어, 횟수) 리스트로. 동률이면 단어 사전순."""
    counts = {}
    for w in text.split():
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])[:n]
