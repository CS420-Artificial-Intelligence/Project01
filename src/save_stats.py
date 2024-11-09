import json
import os
def save_stats(stats: json, filename: str):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
        with open(filename, 'w') as f:
            pass
    stat_line = f'Steps: {stats['steps']}, Weight: {stats['weight']}, Node: {stats['node']}, Time (ms): {stats['time(ms)']}, Memory (MB): {stats['memory(MB)']}\n{stats['solution']}\n'
    is_updated = False
    for i in range(len(lines)):
        if lines[i].strip() == stats['strategy']:
            stat = stat_line.split('\n')
            lines[i + 1] = stat[0] + '\n'
            lines[i + 2] = stat[1] + '\n'
            is_updated = True
            break
    if not is_updated:   
        lines.append(stats['strategy'] + '\n')
        lines.append(stat_line)
    with open(filename, 'w') as f:
        f.writelines(lines)
