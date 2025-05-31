from utils import celsius_to_fahrenheit, fahrenheit_to_celsius
from logger import get_logger

logger = get_logger(__name__)

def main():
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    logger.info(f"{celsius}度C は {fahrenheit}度F です。")

    fahrenheit = 77
    celsius = fahrenheit_to_celsius(fahrenheit)
    logger.info(f"{fahrenheit}度F は {celsius}度C です。")

if __name__ == "__main__":
    main()
