FROM ubuntu:latest

LABEL maintainer="Manian VSS<manianvss@hotmail.com>"

RUN apt -y update \
	&& apt -y upgrade \
	&& apt -y install curl sshpass iputils-ping vim wget netcat net-tools\
	&& apt -y install libpq-dev \ 
	&& apt -y install python3 \
    && apt -y install python-is-python3 python3-pip\	
	&& rm -rf /var/cache/apt/*

COPY test_mgmt /test_mgmt
COPY dashboard/build /test_mgmt/build
COPY scripts/* /test_mgmt

WORKDIR /test_mgmt
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "entrypoint.sh"]
