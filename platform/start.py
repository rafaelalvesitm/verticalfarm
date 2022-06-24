import requests
import json

# Create a service group
reqUrl = "http://localhost:4041/iot/services"

headersList = {
    "Accept": "*/*",
    "fiware-service": "verticalfarm",
    "fiware-servicepath": "/",
    "Content-Type": "application/json",
}

payload = json.dumps(
    {
        "services": [
            {
                "apikey": "4jggokgpepnvsb2uv4s40d59ov",
                "cbroker": "http://orion:1026",
                "entity_type": "led",
                "resource": "/iot/json",
            }
        ]
    }
)

response = requests.request("POST", reqdUrl, data=payload, headers=headersList)

if response.text == "{}":
    print("Service group created")


# Create 3 leds
for i in range(1, 4):

    reqUrl = "http://localhost:4041/iot/devices"

    headersList = {
        "Accept": "*/*",
        "fiware-service": "verticalfarm",
        "fiware-servicepath": "/",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "devices": [
                {
                    "device_id": f"led{i}",
                    "entity_name": f"urn:ngsi-ld:led:{i}",
                    "entity_type": "Led",
                    "protocol": "PDI-IoTA-JSON",
                    "transport": "HTTP",
                    "endpoint": f"http://10.42.0.94:5000/iot/devices/led/{i}",
                    "commands": [
                        {"name": "on", "type": "command"},
                        {"name": "off", "type": "command"},
                    ],
                    "attributes": [],
                    "static_attributes": [
                        {
                            "name": "refRaspberry",
                            "type": "Relationship",
                            "value": "urn:ngsi-ld:Raspberry:001",
                        }
                    ],
                }
            ]
        }
    )

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    if response.text == "{}":
        print(f"Device created: led{i}")

# Create 3 SHT20
for i in range(1, 4):

    reqUrl = "http://localhost:4041/iot/devices"

    headersList = {
        "Accept": "*/*",
        "fiware-service": "verticalfarm",
        "fiware-servicepath": "/",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "devices": [
                {
                    "device_id": f"SHT20{i}",
                    "entity_name": f"urn:ngsi-ld:SHT20:{i}",
                    "entity_type": "SHT20",
                    "protocol": "PDI-IoTA-JSON",
                    "transport": "HTTP",
                    "endpoint": f"http://10.42.0.94:5000/iot/devices/SHT20/{i}",
                    "commands": [],
                    "lazy": [
                        {"object_id": "t", "name": "temperature", "type": "float"},
                        {"object_id": "h", "name": "humidity", "type": "float"},
                    ],
                    "attributes": [],
                    "static_attributes": [
                        {
                            "name": "refRaspberry",
                            "type": "Relationship",
                            "value": "urn:ngsi-ld:Raspberry:001",
                        }
                    ],
                }
            ]
        }
    )

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    if response.text == "{}":
        print(f"Device created: SHT20{i}")

# Create 3 globe valve
for i in range(1, 4):

    reqUrl = "http://localhost:4041/iot/devices"

    headersList = {
        "Accept": "*/*",
        "fiware-service": "verticalfarm",
        "fiware-servicepath": "/",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "devices": [
                {
                    "device_id": f"globe_valve{i}",
                    "entity_name": f"urn:ngsi-ld:globe_valve:{i}",
                    "entity_type": "globe_valve",
                    "protocol": "PDI-IoTA-JSON",
                    "transport": "HTTP",
                    "endpoint": f"http://10.42.0.94:5000/iot/devices/globe_valve/{i}",
                    "commands": [
                        {"name": "on", "type": "command"},
                        {"name": "off", "type": "command"},
                    ],
                    "attributes": [],
                    "static_attributes": [
                        {
                            "name": "refRaspberry",
                            "type": "Relationship",
                            "value": "urn:ngsi-ld:Raspberry:001",
                        }
                    ],
                }
            ]
        }
    )

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    if response.text == "{}":
        print(f"Device created: globe_valve{i}")

# Create 3 flow rate valve
for i in range(1, 4):

    reqUrl = "http://localhost:4041/iot/devices"

    headersList = {
        "Accept": "*/*",
        "fiware-service": "verticalfarm",
        "fiware-servicepath": "/",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "devices": [
                {
                    "device_id": f"flow_rate_valve{i}",
                    "entity_name": f"urn:ngsi-ld:flow_rate_valve:{i}",
                    "entity_type": "Flow_rate_valve",
                    "protocol": "PDI-IoTA-JSON",
                    "transport": "HTTP",
                    "endpoint": f"http://10.42.0.94:5000/iot/devices/flow_rate_valve/{i}",
                    "commands": [],
                    "attributes": [
                        {"object_id": "flow_rate", "name": "flow_rate", "type": "float"}
                    ],
                    "static_attributes": [
                        {
                            "name": "refRaspberry",
                            "type": "Relationship",
                            "value": "urn:ngsi-ld:Raspberry:001",
                        }
                    ],
                }
            ]
        }
    )

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    if response.text == "{}":
        print(f"Device created: flow_rate_valve{i}")

# Create 3 pumps
for i in range(1, 4):

    reqUrl = "http://localhost:4041/iot/devices"

    headersList = {
        "Accept": "*/*",
        "fiware-service": "verticalfarm",
        "fiware-servicepath": "/",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "devices": [
                {
                    "device_id": f"pump{i}",
                    "entity_name": f"urn:ngsi-ld:pump:{i}",
                    "entity_type": "pump",
                    "protocol": "PDI-IoTA-JSON",
                    "transport": "HTTP",
                    "endpoint": f"http://10.42.0.94:5000/iot/devices/pump/{i}",
                    "commands": [
                        {"name": "on", "type": "command"},
                        {"name": "off", "type": "command"},
                    ],
                    "attributes": [],
                    "static_attributes": [
                        {
                            "name": "refRaspberry",
                            "type": "Relationship",
                            "value": "urn:ngsi-ld:Raspberry:001",
                        }
                    ],
                }
            ]
        }
    )

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    if response.text == "{}":
        print(f"Device created: pump{i}")
