# Vision-project
---
## 🎙 Describing images with audio
📌 Project idea and objectives
The "Describing images with audio" project is an artificial intelligence system that analyzes images, generates a text description of them, translates them into Arabic (if necessary), and then converts the text into audio. The project aims to:
✅ Enable visually impaired people to understand image content via audio

✅ Improve the experience of users who prefer listening to reading

✅ Support for Arabic and English to increase effectiveness and use in multiple environments

## 🛠 Details of the models and stages used
The project consists of three main stages:

1️⃣ Image analysis and generation of a text description (Image Captioning)
The BLIP (BlipForConditionalGeneration) model from Hugging Face is used
It analyzes the image and produces an appropriate description in English
2️⃣ Translate the text into Arabic (optional)
Google Translator is used to translate the text if the user chooses Arabic
3️⃣ Convert text to voice (Text-to-Speech - TTS)
gTTS (Google Text-to-Speech) is used to create an audio file for the text
An audio introduction is integrated with the text when Arabic is selected to improve clarity
## 🚀 How to operate the interface
💡 The interface is built using Gradio and is interactive and easy to use

🔹 Steps:

Upload an image with visual content
Choose the language: English or Arabic
Get:
A text description of the image
A sound file that can be played and listened to
📌 After publishing the project on Hugging Face Spaces, it will be possible to play it directly from the browser without the need to download any additional programs

## 🤔 Reason for choosing models
✅ BLIP Image Captioning:

Provides high quality description of images based on advanced deep learning
It was trained on a large dataset, making it powerful in describing image content
✅ Google Translator:

Supports translation between English and Arabic with high accuracy
Easy to use and can be integrated directly into the project
✅ gTTS (Google Text-to-Speech):

Supports Arabic and English with natural voice quality
It can produce light and easy-to-play audio files
✅ Gradio:

Enables easy building of an interactive user interface and supports integration with different models
It is easy to publish the application on Hugging Face Spaces so that anyone can use it without complications
📎 How to run the project locally
Install requirements:

pip install gradio transformers gtts pydub deep-translator pillow torch
Run the app:

python app.py
Open the link that will appear in the terminal to use the interface

## 🌍 Publish to Hugging Face Spaces
Create a new Space on Hugging Face
Upload all project files
Ensure that app.py is running as the main source of the application
Publish the application and make it available to the public
🎯🚀 The result: The project provides a smooth and interactive user experience that combines image analysis, translation, and text-to-speech, which enhances accessibility and usability in various situations

🎉 Enjoy the experience of describing images with audio!

Check out the configuration reference at https://huggingface.co/spaces/aryamaseiri/Description-of-images-by-audio
