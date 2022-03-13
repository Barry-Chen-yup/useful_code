FROM apache/airflow:2.2.1
USER root
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
RUN echo 'root:password' | chpasswd
RUN sed -i '/PasswordAuthentication/d' /etc/ssh/sshd_config
RUN sed -i '/PermitRootLogin/d' /etc/ssh/sshd_config
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN /etc/init.d/ssh start
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
