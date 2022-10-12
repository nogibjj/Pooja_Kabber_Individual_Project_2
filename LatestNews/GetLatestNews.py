import scrapetube
from pytube import YouTube
import os
import whisper
import openai
import warnings

warnings.filterwarnings("ignore")

videos = scrapetube.get_channel("UCupvZG-5ko_eiXAupbDfxWw")
model = whisper.load_model("base")
openai.api_key = os.getenv("OPENAI_API_KEY")

i = 0

for video in videos:
    link = "https://www.youtube.com/watch?v=" + str(video["videoId"])

    try:
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    if yt.length < 200:

        # extract only audio
        audio_only = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = audio_only.download()

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = f"audio_file{i}" + ".mp3"
        os.rename(out_file, new_file)

        print(f"TITLE: {yt.title}")
        result = model.transcribe(new_file)
        news_text = result["text"]

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"{news_text}\n\nTl;dr",
            temperature=0.8,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        print(response["choices"][0]["text"]+"\n")

    i = i + 1

    if i > 40:
        break
