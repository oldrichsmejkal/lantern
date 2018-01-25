import lantern as l
import time
import logging
from ..base import Streaming


class RandomSource(Streaming):
    def run(self):
        while True:
            df = l.bar.sample()
            for i in range(len(df)):
                # logging.info(df.iloc[i].to_json())
                self.on_data(df.iloc[i].to_json())
            time.sleep(1)
