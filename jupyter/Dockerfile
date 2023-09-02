FROM python:3.10-slim

RUN mkdir src 
WORKDIR /src

RUN pip install jupyter==1.0.0

COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
