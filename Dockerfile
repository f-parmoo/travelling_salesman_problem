FROM python:3.8-slim-buster

WORKDIR /travelling_salesman_problem
ADD . /travelling_salesman_problem
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]

