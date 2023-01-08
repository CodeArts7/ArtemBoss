import numpy as np
import math


def stat(strg):
    hours = []
    min = []
    sec = []
    res = []

    s = strg.split(',')

    for i in s:
        i = str(i)
        new_i = i.split('|')

        if new_i[0] == '':
            return new_i[0]
        else:
            hours.append(int(new_i[0]) * 3600)
        min.append(int(new_i[1]) * 60)
        sec.append(int(new_i[2]))

    for i in range(len(hours)):
        res.append(hours[i] + min[i] + sec[i])

    ma_x = max(res)

    mi_n = res[0]
    for i in range(len(res) - 1):
        if mi_n > res[i + 1]:
            mi_n = res[i + 1]

    dip = ma_x - mi_n
    average = math.floor(np.mean(res))
    res = sorted(res)

    if len(res) % 2 == 0:
        median = (res[(len(res) // 2)] + res[(len(res) // 2) - 1]) // 2
    else:
        median = res[(len(res) // 2)]

    dip_h = str(dip // 3600)

    dip_m = str((dip - (dip // 3600) * 3600) // 60)

    dip_s = str(dip - ((dip // 3600) * 3600) - (((dip - (dip // 3600) * 3600) // 60) * 60))

    if int(dip_h) <= 9:
        dip_h = str(dip_h)
        dip_h = '0' + dip_h

    if int(dip_m) <= 9:
        dip_m = str(dip_m)
        dip_m = '0' + dip_m

    if int(dip_s) <= 9:
        dip_s = str(dip_s)
        dip_s = '0' + dip_s

    result_dip = dip_h + '|' + dip_m + '|' + dip_s

    average_h = str(average // 3600)
    average_m = str((average - (average // 3600) * 3600) // 60)
    average_s = str(average - ((average // 3600) * 3600) - (((average - (average // 3600) * 3600) // 60) * 60))

    if int(average_h) <= 9:
        average_h = str(average_h)
        average_h = '0' + average_h

    if int(average_m) <= 9:
        average_m = str(average_m)
        average_m = '0' + average_m

    if int(average_s) <= 9:
        average_s = str(average_s)
        average_s = '0' + average_s

    result_average = average_h + '|' + average_m + '|' + average_s

    median_h = str(median // 3600)
    median_m = str((median - (median // 3600) * 3600) // 60)
    median_s = str(median - ((median // 3600) * 3600) - (((median - (median // 3600) * 3600) // 60) * 60))

    if int(median_h) <= 9:
        median_h = str(median_h)
        median_h = '0' + median_h

    if int(median_m) <= 9:
        median_m = str(median_m)
        median_m = '0' + median_m

    if int(median_s) <= 9:
        median_s = str(median_s)
        median_s = '0' + median_s

    result_median = median_h + '|' + median_m + '|' + median_s

    return f'Range: {result_dip} Average: {result_average} Median: {result_median}'
