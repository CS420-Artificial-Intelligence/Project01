import json
import os
def save_stats(stats: json, filename: str):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
        # create file
        os.mknod(filename)
    stat_line = f'Steps: {stats['steps']}, Weight: {stats['weight']}, Node: {stats['node']}, Time (ms): {stats['time(ms)']}, Memory (MB): {stats['memory(MB)']}\n{stats['solution']}\n'
    for i in range(0, len(lines), 2):
        if lines[i].strip() == stats['strategy']:
            lines[i + 1] = stat_line
            return
    lines.append(stats['strategy'] + '\n')
    lines.append(stat_line)
    with open(filename, 'w') as f:
        f.writelines(lines)
