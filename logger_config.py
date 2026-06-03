import logging
import os
from datetime import datetime

data_log = datetime.now().strftime("%Y\%m\%d")
pasta_log = f'0.log\{data_log}'

os.makedirs(pasta_log, exist_ok=True)

logging.basicConfig(
    filename = f"{pasta_log}\Log_Scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)