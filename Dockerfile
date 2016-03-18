FROM soulshake/aws.cli:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
    ssh \
    curl \
    jq \
    bsdmainutils \
    pssh \
    python-pip \
    man

RUN apt-get install -y wkhtmltopdf

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/user && \
    mkdir -p /etc/sudoers.d && \
    echo "user:x:${uid}:${gid}:user,,,:/home/user:/bin/bash" >> /etc/passwd && \
    echo "user:x:${uid}:" >> /etc/group && \
    echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user && \
    chown ${uid}:${gid} -R /home/user

RUN pip install PyYAML
RUN pip install pdfkit
RUN pip install termcolor
