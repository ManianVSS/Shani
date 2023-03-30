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
COPY webui/build /test_mgmt/build
COPY scripts/* /test_mgmt

WORKDIR /test_mgmt
RUN pip install -r requirements.txt
RUN bash cleandb.sh

ENV DATABASE__NAME=testmgmt
ENV DATABASE__USER=testmgmtadmin
ENV DATABASE__PASSWORD=testmgmtadmin@123
ENV DATABASE__HOST=localhost
ENV DATABASE__PORT=5432

ENV mode=production
ENV DJANGO__bool__DEBUG=False

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver","0.0.0.0:8000 --insecure"]
