import os

data_dir = 'data'
items = os.listdir(data_dir)
classes = [name for name in items if os.path.isdir(os.path.join(data_dir, name))]
counts = {}
for cls in classes:
    cls_path = os.path.join(data_dir, cls)
    files = os.listdir(cls_path)
    counts[cls] = len(files)
print(counts)
for cls, count in counts.items():
    print(f'{cls}: {count}')