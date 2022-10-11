import whisper
model = whisper.load_model("base")
result = model.transcribe("inmyhead.mp3")
print(result["text"])