import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from gtts import gTTS
from pydub import AudioSegment
from deep_translator import GoogleTranslator
from PIL import Image
import torch

# Load the model and transformer
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    "Generate image description in English"
    inputs = processor(images=image, return_tensors="pt")
    caption_ids = model.generate(**inputs, max_length=30)
    return processor.decode(caption_ids[0], skip_special_tokens=True)

def translate_to_arabic(text):
    "Translate the text into Arabic"
    return GoogleTranslator(source="en", target="ar").translate(text)

def text_to_speech(text, language):
    "Convert text to speech without mixing languages"
    file_path = "output.mp3"
    
    if language == "العربية":
        arabic_intro = "هذا وصف للصورة: "
        arabic_caption = translate_to_arabic(text)
        arabic_tts = gTTS(text=arabic_intro, lang="ar")
        caption_tts = gTTS(text=arabic_caption, lang="ar")

        # Save audio files
        arabic_tts.save("arabic_intro.mp3")
        caption_tts.save("caption.mp3")

        # Merge the two sounds
        audio1 = AudioSegment.from_mp3("arabic_intro.mp3")
        audio2 = AudioSegment.from_mp3("caption.mp3")
        combined = audio1 + audio2
        combined.export(file_path, format="mp3")
    
    else:
        tts = gTTS(text=text, lang="en")
        tts.save(file_path)

    return file_path

def process_image(image_path, language):
    "Generate an image description, translate it, and convert it into speech."
    image = Image.open(image_path).convert("RGB")
    caption = generate_caption(image)
    
    if language == "العربية":
        caption = translate_to_arabic(caption)
    
    speech_file = text_to_speech(caption, language)
    return caption, speech_file

# Gradio Interface
iface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="filepath"), gr.Radio(["English", "العربية"], label="Language")],
    outputs=["text", "audio"],
    title="🎙 وصف الصور بالصوت",
    description="📷 ارفع الصورة وسيتم توليد وصف قصير لها وتحويله إلى صوت باللغة المختارة"
)

iface.launch()