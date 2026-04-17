from collections import Counter

def create_bow(tokens_list):
    return dict(Counter(tokens_list))