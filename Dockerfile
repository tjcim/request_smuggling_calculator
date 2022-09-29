FROM python:3.10
EXPOSE 5000
WORKDIR /usr/src/app
ENV PIP_ROOT_USER_ACTION=ignore
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
