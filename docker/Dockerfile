FROM python:3.8.10
COPY . /workspace
WORKDIR /workspace
RUN ["pip3", "install", "-r", "requirements.txt"]
RUN chmod +x opencv_cuda.sh
RUN chmod +x airflow_info.sh
RUN ./opencv_cuda.sh
RUN ./airflow_info.sh
EXPOSE 8080