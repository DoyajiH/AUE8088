from collections import defaultdict
import random
import os

random.seed(42)

txt_path = os.path.join('..', 'kaist-rgbt', 'train-all-04.txt')

with open(txt_path, 'r') as f:
    all_lines = [line.strip() for line in f.readlines()]

# setXX_VXXX 기준으로 시퀀스 분리
seq_dict = defaultdict(list)
for line in all_lines:
    parts = line.split('/')
    if len(parts) < 6:
        continue
    seq = parts[5][:11]  # "set00_V000" ← 이게 시퀀스 ID
    seq_dict[seq].append(line + '\n')

# 시퀀스 기준으로 shuffle → split
keys = list(seq_dict.keys())
random.shuffle(keys)
split_idx = int(len(keys) * 0.8)

train_keys = keys[:split_idx]
val_keys = keys[split_idx:]

train_lines = sum([seq_dict[k] for k in train_keys], [])
val_lines = sum([seq_dict[k] for k in val_keys], [])

# 저장
output_dir = os.path.join('..', 'kaist-rgbt')
with open(os.path.join(output_dir, 'train_split.txt'), 'w') as f:
    f.writelines(train_lines)
with open(os.path.join(output_dir, 'val_split.txt'), 'w') as f:
    f.writelines(val_lines)

print(f"[✔] Train lines: {len(train_lines)}, Val lines: {len(val_lines)}")
