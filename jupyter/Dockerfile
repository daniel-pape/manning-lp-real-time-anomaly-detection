FROM python:3.10-slim

RUN mkdir src 
WORKDIR /src

RUN pip install jupyter

# jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
