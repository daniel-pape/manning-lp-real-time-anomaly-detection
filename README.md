## Milestone 1

At the beginning we are given the following partial solution for the Dockerfile:

```bash
FROM python:3.10-slim

RUN ...
WORKDIR ...

RUN ...

CMD [...]
```

Following the described steps we fill in the placeholders to arrive at the following
intermediate solution:

```bash
FROM python:3.10-slim

RUN mkdir src
WORKDIR /src

RUN pip install jupyter
```

To better understand how the last `CMD` has to be filled in we run bash in interactive
mode with the intermediate Dockerfile and try to run the server with one of the commands
found in the included references:

* Run bash in the container: `docker run -it --entrypoint /bin/bash dp/lp-jupyter`
* Testwise start Jupyter:
```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

The last command works and from it we can fill in the final `CMD` to arrive
at the final Dockerfile.

From this Dockerfile we can build the container using the following command:
```bash
cd jupyter
docker build -t dp/lp-jupyter .
```
Finally, we can run the container:
```bash
docker run -p 8888:8888 dp/lp-jupyter
```



