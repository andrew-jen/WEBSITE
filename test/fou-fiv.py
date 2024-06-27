def find_prefix_keywords(keywords, prefix):
    result = []
    for keyword in keywords:
        if keyword.startswith(prefix):
            result.append(keyword)
    result.sort(key=lambda x: (len(x), x))
    return result