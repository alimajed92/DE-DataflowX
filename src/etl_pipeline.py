import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka import KafkaConsumer, TopicPartition
from json import dumps
from logger.logger import dataFlow_logger
from exceptions.exceptions import dataFlow_Exception
import time
from config import Config
import json
import pandas as pd


# === MQTT Callback ===
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ MQTT connected successfully.")
        client.subscribe("#")
    else:
        print(f"❌ MQTT connection failed. Return code {rc}")


def on_message(client, userdata, msg):
    print(f"📩 MQTT message received on topic '{msg.topic}': {msg.payload.decode()}")

    kafka_broker = "127.0.0.1:9092"
    kafka_topic = "Data-test"

    try:
        # Create Kafka producer
        producer = KafkaProducer(
            bootstrap_servers=kafka_broker,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

        # Forward the MQTT message payload to Kafka
        producer.send(kafka_topic, msg.payload.decode())
        producer.flush()
        print(f"✅ Message forwarded to Kafka topic '{kafka_topic}'")

    except Exception as e:
        print(f"❌ Error sending to Kafka: {e}")


# === MQTT Connection ===
def connect_to_mqtt(broker_host: str, broker_port: int = 1883) -> mqtt.Client:
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    try:
        mqtt_client.connect(broker_host, int(broker_port), 60)
    except Exception as e:
        print(f"❌ Failed to connect to MQTT broker: {e}")
        raise

    return mqtt_client


# === Send DataFrame to MQTT ===
def sending_to_mqtt(mqtt_client: mqtt.Client, df: pd.DataFrame, topic: str) -> None:
    if not topic:
        raise Exception("MQTT topic must be specified.")

    mqtt_client.loop_start()

    for _, row in df.iterrows():
        payload = json.dumps(row.to_dict())
        mqtt_client.publish(topic, payload)
        print(f"📤 Published to MQTT topic '{topic}': {payload}")
        time.sleep(1)

    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("🔌 Disconnected from MQTT broker.")
