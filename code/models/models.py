from transformers import AutoImageProcessor, AutoModelForObjectDetection
import torch

class TableTransformer:
    def __init__(self):
        self.processor = AutoImageProcessor.from_pretrained("microsoft/table-transformer-detection")
        self.model = AutoModelForObjectDetection.from_pretrained("microsoft/table-transformer-detection")

    def detect_tables(self, image):
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs
