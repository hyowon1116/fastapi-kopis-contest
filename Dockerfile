FROM python:3.9
ENV PYTHONUNBUFFEREDdoc 1

RUN apt-get update && apt-get clean

COPY ./requirements /code/requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r code/requirements/requirements.txt

COPY ./src /code/src
WORKDIR /code

# we don't need core dump file.
RUN ulimit -c 0

ENTRYPOINT [ \
            "uvicorn", \
            "src.app:app", \
            "--proxy-headers", \ 
            "--host", "0.0.0.0", \ 
            "--port", "8000" \
]