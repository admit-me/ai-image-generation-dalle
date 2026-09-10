import base64
import io
from pathlib import Path

import cv2
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from openai import OpenAI


def generate_image(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '').strip()
        if not prompt:
            context['error'] = 'Please enter a prompt.'
            return render(request, 'generator/index.html', context)
        if not settings.OPENAI_API_KEY:
            context['error'] = 'OPENAI_API_KEY is not configured.'
            return render(request, 'generator/index.html', context)
        try:
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            result = client.images.generate(model='gpt-image-1', prompt=prompt, size='1024x1024')
            image_bytes = base64.b64decode(result.data[0].b64_json)
            array = __import__('numpy').frombuffer(image_bytes, dtype='uint8')
            image = cv2.imdecode(array, cv2.IMREAD_COLOR)
            if image is None:
                raise ValueError('Generated image could not be decoded.')
            output_dir = Path(settings.MEDIA_ROOT) / 'generated'
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / 'generated.png'
            cv2.imwrite(str(output_path), image)
            context['image_url'] = settings.MEDIA_URL + 'generated/generated.png'
            context['prompt'] = prompt
        except Exception as exc:
            context['error'] = f'Generation failed: {exc}'
    return render(request, 'generator/index.html', context)
