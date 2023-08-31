FROM alpine:3.18.3

WORKDIR /volume

RUN apk update && \
		apk add --no-cache python3~3.11 python3-dev~3.11 py3-pip gcc build-base linux-headers git wget
RUN wget https://raw.githubusercontent.com/amazon-science/patchcore-inspection/main/requirements.txt && \
		pip install -r requirements.txt
RUN pip install jupyter torchmetrics==1.1.1

COPY startup.sh .
ENTRYPOINT ash -c startup.sh
