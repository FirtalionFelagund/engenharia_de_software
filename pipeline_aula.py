class DataPipeline:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data = [d for d in self.data if d is not None]
        print(f"Dados limpos: {self.data}")

    def normalize_data(self):
        max_value = max(self.data)
        self.data = [d / max_value for d in self.data]
        print(f"Dados normalizados: {self.data}")

# Uso da pipeline de dados
pipeline = DataPipeline([10, None, 30, 20])
pipeline.clean_data()
pipeline.normalize_data()