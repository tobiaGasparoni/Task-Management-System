#!/bin/bash

case $1 in

  clean)
    echo "you want to restart from scratch\n"
    docker rm -f task-management-system_web_1
    docker rm -f task-management-system_redis_1
    docker rm -f task-management-system_postgres_1
    docker rmi -f task-management-system_web:latest
    ;;

  *)
    echo -n "unknown command"
    ;;
esac