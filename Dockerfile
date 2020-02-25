FROM python:3.7
RUN pip3 install \
    jupyterhub \
    notebook \
    jupyter-server-proxy \
    streamlit

# create a user, since we don't want to run as root
RUN useradd -m jovyan
ENV HOME=/home/jovyan
WORKDIR $HOME
USER jovyan

RUN mkdir /tmp/proxyconfig

COPY setup.py /tmp/proxyconfig
COPY streamlitproxy.py /tmp/proxyconfig

RUN cd /tmp/proxyconfig && pip3 install .

CMD ["jupyterhub-singleuser"]

