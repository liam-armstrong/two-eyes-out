#!/bin/bash

set -e

PROD_UP="prod"
DEV_UP="dev"
PROD_DOWN="prod-down"
DEV_DOWN="dev-down"
SERVER="ssh"

print_usage() {
  echo "USAGE: ./run.sh [ $PROD_UP | $DEV_UP | $STACK_DOWN | $DEV_DOWN | $SERVER ]"
  echo "$PROD_UP: Run the full stack in a production environment"
  echo "$DEV_UP: Run the full stack in a developer environment"
  echo "$PROD_DOWN: Tear down prod containers"
  echo "$DEV_DOWN: Tear down dev containers"
  echo "$SERVER: Connect to AWS EC2 instance"
}

check_docker() {
  docker --version > /dev/null
  STATUS=$?
  if [[ $STATUS != 0 ]]; then
    echo "You need to install docker CLI!"
    exit 1
  fi
  if [ ! -f ".env" ]; then
    echo ".env is not configured"
    exit 1
  fi
}

DESIRED_PROTOCOL=$1

if [[ $DESIRED_PROTOCOL == $PROD_UP ]]; then
  check_docker
  docker-compose -f config/full-stack-prod.yml up --build --force-recreate
  echo "Remember to tear down the stack!"
  exit 0
elif [[ $DESIRED_PROTOCOL == $DEV_UP ]]; then
  check_docker
  docker-compose -f config/full-stack-dev.yml up --build --force-recreate
  echo "Remember to tear down the stack!"
  exit 0
elif [[ $DESIRED_PROTOCOL == $PROD_DOWN ]]; then
  check_docker
  docker-compose -f config/full-stack-prod.yml down
  exit 0
elif [[ $DESIRED_PROTOCOL == $DEV_DOWN ]]; then
  check_docker
  docker-compose -f config/full-stack-dev.yml down
  exit 0
elif [[ $DESIRED_PROTOCOL == $SERVER ]]; then
  ssh -i "key.pem" ec2-user@ec2-3-87-134-115.compute-1.amazonaws.com
else
  print_usage
  exit 0
fi