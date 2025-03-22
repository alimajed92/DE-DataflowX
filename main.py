from logger.logger import dataFlow_logger
from exceptions.exceptions import dataFlow_Exception
import os
from config import Config
import config as cfg
from src.etl_pipeline import (
    connect_to_mqtt,
    sending_to_mqtt,
)
from src.data_processing import process_csv_data

# reriving env variables
mqtt_host = Config.MQTT_BROKER_HOST
mqtt_port = Config.MQTT_BROKER_PORT
# mqtt_topic=Config.MQTT_TOPIC if we have defrent topic please add this


if __name__ == "__main__":
    cfg.Config.validate()
    cfg.Config.display()
    mqtt_client = connect_to_mqtt(mqtt_host, mqtt_port)
    df = process_csv_data()
    if mqtt_client is not None:
        dataFlow_logger.info(
            f"Connected to MQTT broker and mqtt_client created at {mqtt_client} "
        )
    else:
        dataFlow_logger.error("Failed to connect to MQTT broker")
    # sending data
    sending_to_mqtt(mqtt_client, df, topic="weather_data")
    # mqtt_to_kafka(mqtt_client)
