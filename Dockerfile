FROM python:3.12.3 AS python-build
RUN pip install mysqlclient

FROM python:3.12.3-slim-bullseye
WORKDIR /app
EXPOSE 5000
COPY --from=python-build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
RUN apt-get update && apt-get install -y libmariadb3
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

RUN chmod a+x *.sh
ENTRYPOINT ["./app.sh"]