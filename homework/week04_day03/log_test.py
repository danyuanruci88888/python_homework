import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("这是一条 info 日志")
logging.warning("这是一条 warning 日志")
logging.error("这是一条 error 日志")