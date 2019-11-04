#!/bin/sh -eu
echo -n "Preparing container... "
CID=$(docker run -d --rm -it mcr.microsoft.com/azure-functions/python /bin/bash)
docker cp $(cd $(dirname $0) && pwd) ${CID}:/tmp/ > /dev/null 2>&1
echo "done"
echo -n "Installing necessary libraries into container... "
docker exec ${CID} sh -c 'mkdir -p /tmp/lib && apt update && apt install $(cat /tmp/utils/additional_packages.txt | grep -v "^#" | tr "\n" " ") -y && cp -L $(ldconfig -p | grep -E "($(cat /tmp/utils/necessary_libraries.txt | grep -v "^#" | tr "\n" "|" | sed -E "s/\|{1,}$//"))" | sed -E "s/.* ([^ ]+$)/\1/") /tmp/lib' > /dev/null 2>&1
echo "done"
echo -n "Copy libraries from container... "
docker cp ${CID}:/tmp/lib . > /dev/null 2>&1
echo "done"
echo -n "Shutting down container... "
docker kill ${CID} > /dev/null 2>&1
echo "done"
echo "Finished."