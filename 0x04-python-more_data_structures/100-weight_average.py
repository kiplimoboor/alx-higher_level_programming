#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_weight_sum = sum(list(map((lambda x: x[0] * x[1]), my_list)))
    weight_sum = sum(list(map((lambda x: x[1]), my_list)))
    return score_weight_sum / weight_sum
