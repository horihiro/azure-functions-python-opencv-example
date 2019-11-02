@echo off
for /f "usebackq" %%A in (`docker run -d --rm -it mcr.microsoft.com/azure-functions/python /bin/bash`) do set CID=%%A
docker exec %CID% sh -c "apt update && apt install libglib2.0-0 -y && cp -L $(ldconfig -p | grep -E 'libg(thread|lib)-2.0.so.0' | sed -E 's/.* ([^ ]+$)/\1/') /tmp/"
docker cp %CID%:/tmp/ ./lib
docker kill %CID%
