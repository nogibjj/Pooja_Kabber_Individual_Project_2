FROM python:3.10
WORKDIR /

RUN apt-get update
RUN apt-get install -y ffmpeg
RUN pip3 install --upgrade pip
COPY requirements.txt /tmp/
RUN pip3 install --trusted-host pypi.python.org -r /tmp/requirements.txt
RUN pip install git+https://github.com/openai/whisper.git 
RUN rm /tmp/requirements.txt
RUN mkdir /home/get_news/
WORKDIR /home/get_news/
COPY GetLatestNews.py /home/get_news/
COPY latest_news_cli.py /home/get_news/
COPY test_file.py /home/get_news/
RUN chmod +x latest_news_cli.py
RUN export PATH=/home/get_news:$PATH
RUN echo 'alias getnews="python3 latest_news_cli.py"' >> ~/.bashrc