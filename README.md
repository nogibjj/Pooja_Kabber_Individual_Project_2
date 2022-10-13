# Command Line Tool For Latest News


## Architecture Diagram

This project uses Whisper, OpenAI, DockerHub and Github Codespaces to build a command-line tool that gives short summaries of latest news by transcribing and summarizing videos from CNN's YouTube channel.

![DataEngineeringProject2](https://user-images.githubusercontent.com/112586823/195504031-7220aab8-52a6-4853-9130-964d8cd3f69f.jpg)

## Media

## User Instructions

To run the docker image, type in terminal:

`$docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -it poojakabber/dataengineeringproject2:latest ./latest_news_cli.py`
