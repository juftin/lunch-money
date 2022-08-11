ARG BASE_IMAGE
FROM ${BASE_IMAGE:-python:3.9-slim}

MAINTAINER Justin Flannery "juftin@juftin.com"

RUN python -m pip install --upgrade pip
COPY pyproject.toml README.md /tmp/lunchable/
COPY lunchable/ /tmp/lunchable/lunchable/
RUN pip install /tmp/lunchable/[splitlunch] && rm -rf /tmp/lunchable

RUN apt-get update && apt-get install -y jq && apt-get clean

SHELL ["/bin/bash", "-c"]

RUN _LUNCHABLE_COMPLETE=bash_source lunchable > ${HOME}/.lunchable-complete.bash && \
    echo "[[ ! -f ${HOME}/.lunchable-complete.bash ]] || source ${HOME}/.lunchable-complete.bash" >> /root/.bashrc

CMD ["lunchable", "--help"]
