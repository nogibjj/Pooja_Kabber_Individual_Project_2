[![Command-Line Tool](https://github.com/nogibjj/Pooja_Kabber_Individual_Project_2/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Pooja_Kabber_Individual_Project_2/actions/workflows/main.yml)

# Command-Line Tool For Latest News

## Description

This command-line tool allows you to get news shorts from popular news channels like CNN and BBC on the terminal.

## Architecture Diagram

The project uses Whisper, OpenAI, DockerHub and Github Codespaces to build a command-line tool that gives short summaries of latest news by transcribing and summarizing videos from popular news programs' YouTube channels. The tool is also Dockerized and pushed to DockerHub. 

![DataEngineeringProject2](https://user-images.githubusercontent.com/112586823/195504031-7220aab8-52a6-4853-9130-964d8cd3f69f.jpg)

## Media

## Usage

To run the tool, type in terminal:

```
$docker run -e OPENAI_API_KEY=<OPENAI_API_KEY> -it poojakabber/dataengineeringproject2:latest ./latest_news_cli.py
```

where `<OPENAI_API_KEY>` should be replaced with the OpenAI api key you create.

### Options

There are four configurable options for this tool:

1. `--channel`: This option lets you define which news program you want to receive news shorts from. This can be chosen from cnn, bbc, msnbc, aljazeera and ndtv. This is by default cnn.
2. `--length`: This option lets you define the maximum length of every news short. It must lie between 40 and 100 characters. This is by default 60.
3. `--n`: This option allows you to configure how many news shorts you want displayed. It must lie between 1 and 40. This is by default 10.
4. `--title`: This option allows you to choose whether or not to see the title of the news short. This is by default False.

### Example

Below is an example usage:

```
$docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -it poojakabber/dataengineeringproject2:latest ./latest_news_cli.py --channel bbc --length 40 --n 5 --title
```

This will display 5 news shorts derived from BBC's Youtube channel with their titles, each of maximum length of 40 characters.

```
TITLE: What will Russian President Vladimir Putin do next in Ukraine? - BBC News
 Putin is an authoritarian leader of a nuclear power, and he's not going to back down any time soon.

TITLE: Alex Jones told to pay $965m damages to Sandy Hook shooting victims’ families – BBC News
 Alex Jones was ordered to pay $100 million to the families of Sandy Hook victims after he claimed the shooting was a hoax.

TITLE: Ukraine war: Countries pledge help as Russian missile strikes continue - BBC News
 The US and its allies are pledging to provide more military support to Ukraine in the form of weapons and equipment. This comes as Russian forces have intensified their attacks on Ukrainian civilians and infrastructure.

TITLE: G7 countries to back Ukraine ‘for as long as it takes’ - BBC News
 The Russian military has been carrying out missile strikes in Ukraine for the past two days, causing damage to infrastructure and civilian casualties.
President Zelensky has appealed to NATO.

TITLE: Texas parents storm school over shooting fears after Uvalde - BBC News
 High anxiety around potential school shootings is linked to the collective trauma experienced after the Uvaldi shooting.
