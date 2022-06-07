 #!/bin/bash
#
#  Command Line Interface to start and setup the platform
# 

set -e

if (( $# < 1 )); then echo "Wrong umber of parameters"
	echo "usage: services [help|start|stop]"
	exit 1
fi

displayServices () {
	echo ""
	docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
	echo ""
}

waitForOrion () {
	echo -e "\n⏳ Waiting for \033[1;34mOrion\033[0m to be available\n"

	while ! [ `docker inspect --format='{{.State.Health.Status}}' fiware-orion` == "healthy" ]
	do
	  echo `docker inspect --format='{{.State.Health.Status}}' fiware-orion`
	  echo -e "Context Broker HTTP state: " `docker inspect --format='{{.State.Health.Status}}' fiware-orion` " (waiting for healthy)"
	  sleep 1
	done
}

waitForioTAgentJson () {
	echo -e "\n⏳ Waiting for \033[1;34mOrion\033[0m to be available\n"

	while ! [ `docker inspect --format='{{.State.Health.Status}}' fiware-orion` == "healthy" ]
	do
	  echo `docker inspect --format='{{.State.Health.Status}}' fiware-orion`
	  echo -e "Orion Context Broker status: " `docker inspect --format='{{.State.Health.Status}}' fiware-orion` " (waiting for healthy)"
	  sleep 1
	done
}

waitForMongoDB () {
	echo -e "\n⏳ Waiting for \033[1mMongoDB\033[0m to be available\n"
	while ! [ `docker inspect --format='{{.State.Health.Status}}' db-mongo` == "healthy" ]
	do 
		echo -e "MongoDB status: " `docker inspect --format='{{.State.Health.Status}}' db-mongo` " (waiting for healthy)"
		sleep 1
	done
}

waitForIoTAgentJSON () {
	echo -e "\n⏳ Waiting for \033[1;36mIoT-Agent-JSON\033[0m to be available\n"
	while ! [ `docker inspect --format='{{.State.Health.Status}}' fiware-iot-agent-json` == "healthy" ]

	do 
	  echo -e "IoT Agent HTTP state: " `docker inspect --format='{{.State.Health.Status}}' fiware-iot-agent-json` " (waiting for healthy)"
	  sleep 1
	done
}


command="$1"
case "${command}" in
	"help")
		echo "usage: services [help|start|stop]"
		;;
	"start")
		echo -e "Starting containers\n"
		docker compose up -d
		waitForIoTAgentJSON
		waitForMongoDB
		waitForOrion
		displayServices
		echo -e "Creating entities in Orion Context Broker and IoT Agent JSON"
		python3 start.py
		;;
	"stop")
		echo -e "Stopping containers\n"
		docker-compose down
		;;
	*)
		echo "Command not Found."
		echo "usage: services [help|start|stop]"
		exit 127;
		;;
esac