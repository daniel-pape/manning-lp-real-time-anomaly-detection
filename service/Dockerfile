FROM python:3.10-slim

RUN mkdir src
WORKDIR /src

RUN mkdir service
COPY service ./service
RUN pip install -r ./service/requirements.txt
CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8000"]
