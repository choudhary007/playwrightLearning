import logging

logging.basicConfig(
    filename="test_simple.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("THIS IS A TEST LOG")
print("Done")