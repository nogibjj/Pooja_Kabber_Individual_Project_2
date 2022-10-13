# Command Line Tool For Latest News

## Description

This command-line tool allows you to get news shorts from popular news channels like CNN and BBC on the terminal.

## Architecture Diagram

The project uses Whisper, OpenAI, DockerHub and Github Codespaces to build a command-line tool that gives short summaries of latest news by transcribing and summarizing videos from popular news programs' YouTube channels. The tool is also Dockerized and pushed to DockerHub. 

![DataEngineeringProject2](https://user-images.githubusercontent.com/112586823/195504031-7220aab8-52a6-4853-9130-964d8cd3f69f.jpg)

## Media

## Usage

To run the tool, type in terminal:

`$docker run -e OPENAI_API_KEY=<OPENAI_API_KEY> -it poojakabber/dataengineeringproject2:latest ./latest_news_cli.py`

where `<OPENAI_API_KEY>` should be replaced with the OpenAI api key you create.

### Options

There are four configurable options for this tool:

1. '--channel': This option lets you define which news program you want to receive news shorts from. This can be chosen from cnn, bbc, msnbc, aljazeera and ndtv.
2. '--length': This option lets you define the maximum length of every news short. It must lie between 40 and 100 characters.
3. '--n': This option allows you to configure how many news shorts you want displayed. It must lie between 1 and 40.
4. '--title': This option allows you to choose whether or not to see the title of the news short.

## Example
