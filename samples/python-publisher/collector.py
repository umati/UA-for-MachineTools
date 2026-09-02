#SPDX-License-Identifier: MIT
import time
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import json

load_dotenv()

MACHINE_NAME = os.getenv("MACHINE_NAME", "SvenShowcaseMachineTool")
COLLECTOR_MODE = os.getenv("COLLECTOR_MODE", "print").lower()
OUTPUT_DIR = "verbose_messages/data"
TOPIC_PREFIX = os.getenv("TOPIC_PREFIX", "opcua/umati/v3/json")
COMPANY_ID = os.getenv("COMPANY_ID", "+")
PUBLISHER_ID = os.getenv("PUBLISHER_ID", "+")

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected successfully to MQTT Broker!")
        
        # Subscribe to both data and metadata for the given identity
        #topic_pattern = #f"{TOPIC_PREFIX}/+/{COMPANY_ID}/{PUBLISHER_ID}/{MACHINE_NAME}/#"
        client.subscribe("opcua/umati/v3/json/data/verbose/server-cpp-dev/#")
        
        #print(f"Subscribed to: {topic_pattern}")
        print(f"Mode: {COLLECTOR_MODE}")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        payload_string = msg.payload.decode("utf-8").strip()
        
        try:
            parsed_payload = json.loads(payload_string)
        except json.JSONDecodeError:
            parsed_payload = payload_string

        topic = msg.topic

        if COLLECTOR_MODE == "save":
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)
            
            # Create a safe filename from the topic
            filename_safe_topic = topic.replace("/", "_")
            if "/metadata/" in topic:
                filename = f"metadata_{filename_safe_topic}.json"
            else:
                filename = f"data_{filename_safe_topic}.json"

            filepath = os.path.join(OUTPUT_DIR, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump({
                    "topic": topic,
                    "payload": parsed_payload
                }, f, indent=4)
            print(f"Saved message to {filepath}")
            
        else:
            # Default to "print" mode
            print(f"\n--- [Topic: {topic}] ---")
            if isinstance(parsed_payload, dict):
                print(json.dumps(parsed_payload, indent=4))
            else:
                print(parsed_payload)

    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, transport="websockets")
client.ws_set_options(path="/ws")
client.tls_set()
username = os.getenv("MQTT_USER")
password = os.getenv("MQTT_PASSWORD")
if username and password:
    client.username_pw_set(username=username, password=password)

client.on_connect = on_connect
client.on_message = on_message

MQTT_HOST = os.getenv("MQTT_HOST")
PORT = int(os.getenv("MQTT_PORT", 1883))

print(f"Connecting to {MQTT_HOST}:{PORT}...")

try:
    client.connect(MQTT_HOST, PORT, keepalive=10)
    client.loop_forever()
except KeyboardInterrupt:
    print("\nStopping MQTT Client...")
except Exception as e:
    print(f"Failed to connect: {e}")
finally:
    client.disconnect()
