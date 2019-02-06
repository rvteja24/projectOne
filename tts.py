import pyttsx3;
import ocr
engine = pyttsx3.init()
engine.say(ocr.textContent)
engine.runAndWait()
print("Done!")