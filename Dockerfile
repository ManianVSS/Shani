FROM ubuntu:latest

LABEL maintainer="Manian VSS<manianvss@hotmail.com>"

RUN apt -y update \
	&& apt -y upgrade \
	&& apt -y install curl sshpass iputils-ping vim wget netcat net-tools\
	&& apt -y install python3 \
	&& apt -y install python-is-python3 python3-pip\
	&& apt -y install libpq-dev \
	&& rm -rf /var/cache/apt/*

COPY test_mgmt /test_mgmt
# COPY webui/build /test_mgmt/build
COPY scripts/* /test_mgmt

WORKDIR /test_mgmt
COPY test_mgmt/dev-config.yaml.example /test_mgmt/config.yaml
RUN pip install -r requirements.txt
RUN bash cleandb.sh

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000","--insecure"]
