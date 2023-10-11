#!/usr/bin/pyhton3
def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    sort = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
    return sort[0][0]
