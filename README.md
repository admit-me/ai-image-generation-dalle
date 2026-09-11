# AI-Powered Image Generation from Text Descriptions

> Django web application integrating an AI image-generation API with image processing.

This project converts natural-language prompts into generated images through an API-driven workflow. It demonstrates Django application structure, third-party API integration, prompt handling, file processing and environment-based configuration.

## Features

- Django web interface for entering prompts
- OpenAI image-generation API integration
- Local image download/storage
- OpenCV-based image resizing/processing
- Pillow image-file handling
- Environment-variable based API key configuration

## Tech Stack

**Python • Django • OpenAI API • OpenCV • Pillow • HTML/CSS**

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

Add your API key to `.env`:

```text
OPENAI_API_KEY=your_api_key_here
```

Never commit a real API key to GitHub.

## Project Structure

```text
ai-image-generation-dalle/
├── image_generator/
├── generator/
│   ├── urls.py
│   ├── views.py
│   └── templates/
├── media/
├── manage.py
├── requirements.txt
└── .env.example
```

## Skills Demonstrated

**Django • Python • API Integration • Backend Development • Prompt Handling • Image Processing • Environment Configuration • Git/GitHub**

## Author

**Meka Praveen Kumar Reddy**  
Python / Django Developer
