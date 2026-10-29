import os
from PIL import Image
from torch.utils.data import Dataset


class GarbageDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform

        self.classes = sorted([
            d for d in os.listdir(data_dir)
            if os.path.isdir(os.path.join(data_dir, d))
        ])

        self.samples = []
        for idx, cls in enumerate(self.classes):
            cls_path = os.path.join(data_dir, cls)
            for fname in os.listdir(cls_path):
                if fname.lower().endswith((".jpg", ".jpeg", ".png")):
                    self.samples.append((os.path.join(cls_path, fname), idx))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        image = Image.open(path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label


if __name__ == "__main__":
    ds = GarbageDataset("data")
    print("Классы:", ds.classes)
    print("Всего картинок:", len(ds))
    print("Первый элемент:", ds[0])
    print("Метка первого:", ds[0][1])