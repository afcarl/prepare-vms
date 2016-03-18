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
RUN pip install pdfkit

RUN pip install termcolor
RUN pip install PyYAML
