from dotenv import load_dotenv
import os
from pathlib import Path
from exceptions.exceptions import dataFlow_Exception
from logger.logger import dataFlow_logger

# Load environment variables
load_dotenv()


class Config:
    """Application Configuration Class"""

    BASE_DIR = Path(__file__).resolve().parent
    MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "127.0.0.1")
    MQTT_BROKER_PORT = os.getenv("MQTT_BROKER_PORT", 1883)
    DATA_FOLDER = BASE_DIR / "Data"

    @classmethod
    def validate(cls):
        """Ensure that required settings are available."""
        dataFlow_logger.info("Validating Configuration...")
        try:
            if cls.MQTT_BROKER_HOST is None:
                raise dataFlow_Exception(
                    "MQTT_BROKER_HOST is not set in environment variables"
                )

            if cls.MQTT_BROKER_PORT is None:
                raise dataFlow_Exception(
                    "MQTT_BROKER_PORT is not set in environment variables"
                )

            if cls.DATA_FOLDER is None:
                raise dataFlow_Exception(
                    "Foldername is not set in environment variables"
                )

        except dataFlow_Exception as e:
            dataFlow_logger.error(f"Configuration Validation Error: {str(e)}")
            raise

    @classmethod
    def display(cls):
        """Display configuration for debugging purposes."""
        # Define ANSI color codes
        BLUE = "\033[94m"  # Blue for labels
        YELLOW = "\033[93m"  # Yellow for variable values
        RESET = "\033[0m"  # Reset color to default
        dataFlow_logger.info("Configuration Details:")
        dataFlow_logger.info(
            f"{YELLOW}Base Directory:{RESET} {BLUE}{cls.BASE_DIR}{RESET}"
        )
        dataFlow_logger.info(
            f"{YELLOW}MQTT_BROKER_HOST:{RESET} {BLUE}{cls.MQTT_BROKER_HOST}{RESET}"
        )
        dataFlow_logger.info(
            f"{YELLOW}MQTT_BROKER_PORT:{RESET} {BLUE}{cls.MQTT_BROKER_PORT}{RESET}"
        )


if __name__ == "__main__":
    # Config.validate()
    # Config.display()
    pass
