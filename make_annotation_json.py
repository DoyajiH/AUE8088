import os
import json

# 경로 설정
val_txt = os.path.join('..', 'kaist-rgbt', 'val_split.txt')
image_root = os.path.join('..', 'kaist-rgbt', 'train', 'images')
label_root = os.path.join('..', 'kaist-rgbt', 'train', 'labels')

output_json = 'KAIST_annotation.json'
annotation_list = []

# 파일 읽기
with open(val_txt, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

for line in lines:
    filename = os.path.basename(line)
    name = os.path.splitext(filename)[0]

    # 레이블 경로: .txt 파일
    label_path = os.path.join(label_root, name + '.txt')
    if not os.path.exists(label_path):
        continue

    # 이미지 경로
    image_path = os.path.join(image_root, name + '.jpg')

    with open(label_path, 'r') as lf:
        annotations = []
        for row in lf.readlines():
            parts = row.strip().split()
            if len(parts) != 5:
                continue
            cls_id, cx, cy, w, h = map(float, parts)
            x = cx - w / 2
            y = cy - h / 2
            annotations.append({
                "category": "person",
                "bbox": [x, y, w, h]
            })

    annotation_list.append({
        "image_path": image_path.replace('\\', '/'),
        "annotations": annotations
    })

# JSON 저장
with open(output_json, 'w') as f:
    json.dump(annotation_list, f, indent=2)

print(f"[✔] Saved {len(annotation_list)} annotations to {output_json}")
