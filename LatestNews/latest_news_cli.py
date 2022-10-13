#!/usr/bin/env python


from GetLatestNews import get_news
import click


@click.command()
@click.option("--channel", default="cnn", help="Choose the news channel")
@click.option("--length", type=int, default=60, help="Length of summary")
@click.option("--n", type=int, default=10, help="Number of shorts")
@click.option("--title", is_flag=True, help="Print title of news video")
def main(channel, length, n, title):

    if not channel in ["cnn", "bbc", "msnbc", "aljazeera", "ndtv"]:
        channel = "cnn"

    if (length > 100) or (length < 40):
        length = 60

    if (n < 1) or (n > 40):
        n = 10

    get_news(channel, length, n, title)


if __name__ == "__main__":
    main()
