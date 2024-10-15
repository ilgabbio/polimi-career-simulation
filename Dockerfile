FROM python:3.10
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y libgl1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN pip install pipenv==2022.3.28 build==1.1.1

COPY Pipfile Pipfile.lock .

RUN pipenv sync --system --pre

COPY workshop.ipynb /workspace/

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]