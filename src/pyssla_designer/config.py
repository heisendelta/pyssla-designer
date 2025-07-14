import json

class Config:
    def __init__(self, config_file='config/config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def __getitem__(self, key):
        return self.config[key]

config = Config()
