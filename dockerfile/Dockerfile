FROM mltooling/ml-workspace-gpu:0.13.2
RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        build-essential \
        apt-utils \
        curl \
        rsync \
        netcat \
    && apt-get install -yqq --no-install-recommends \
        vim \
        openssh-server
RUN apt install openssh-server -y
RUN echo 'root:password' | chpasswd
RUN echo "Port 22" >> /etc/ssh/sshd_config
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
EXPOSE 8080 22
CMD /etc/init.d/ssh restart