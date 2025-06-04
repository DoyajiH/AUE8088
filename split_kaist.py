from collections import defaultdict
import random
import os

random.seed(42)

# kaist-rgbt 폴더에 있는 파일 경로로 이동
txt_path = os.path.join('..', 'kaist-rgbt', 'train-all-04.txt')

with open(txt_path, 'r') as f:
    all_lines = f.readlines()

# 시퀀스 단위 그룹화
seq_dict = defaultdict(list)
for line in all_lines:
    line = line.strip()
    seq = line.split('/')[0]
    seq_dict[seq].append(line + '\n')

# 시퀀스 단위 분할
keys = list(seq_dict.keys())
random.shuffle(keys)
split_idx = int(len(keys) * 0.8)
train_keys = keys[:split_idx]
val_keys = keys[split_idx:]

train_lines = sum([seq_dict[k] for k in train_keys], [])
val_lines = sum([seq_dict[k] for k in val_keys], [])

# 결과 저장 (aue8088 폴더에)
with open('train_split.txt', 'w') as f:
    f.writelines(train_lines)

with open('val_split.txt', 'w') as f:
    f.writelines(val_lines)

print(f"[✔] Train lines: {len(train_lines)}, Val lines: {len(val_lines)}")
