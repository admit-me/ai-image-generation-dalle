# AI-Powered Image Generation from Text Descriptions

A Django web application that converts natural-language prompts into images using OpenAI's image generation API. OpenCV is used for basic image processing and Pillow handles image files.

## Features
- Django web interface for entering prompts
- OpenAI image generation integration
- Local image download/storage
- OpenCV-based image metadata/resize processing
- Environment-variable based API key configuration
- Simple, clean project structure

## Tech Stack
Python, Django, OpenAI API, OpenCV, Pillow, HTML/CSS

## Setup

```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux
python manage.py migrate
python manage.py runserver
```

Add your OpenAI API key to `.env`:

```text
OPENAI_API_KEY=your_api_key_here
```

Open `http://127.0.0.1:8000/` in your browser.

## Project Structure

```text
ai-image-generation-dalle/
├── image_generator/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── generator/
│   ├── urls.py
│   ├── views.py
│   └── templates/generator/index.html
├── media/
├── manage.py
├── requirements.txt
└── .env.example
```

## Security
Never commit a real API key. `.env` is intentionally excluded through `.gitignore`.

## Portfolio Note
This project demonstrates API integration, backend development, prompt handling, image processing, and Django application structure.