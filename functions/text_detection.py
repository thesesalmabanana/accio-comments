def match_keywords(text, keyword_conditions):
    text = text.lower()
    matched_labels = set()
    matched_keywords = set()

    for label, (group1, group2) in keyword_conditions.items():
        g1 = [kw for kw in group1 if kw in text]
        g2 = [kw for kw in group2 if kw in text]
        if g1 and g2:
            matched_labels.add(label)
            matched_keywords.update(g1 + g2)

    return list(matched_labels), list(matched_keywords)