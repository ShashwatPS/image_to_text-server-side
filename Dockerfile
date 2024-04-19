FROM python:3.7-slim

WORKDIR /src

COPY . .

RUN python pip install fastapi uvicorn python-multipart google-generativeai python-dotenv ipython pillow numpy scipy scikit-learn pandas nltk

EXPOSE 3000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","3000"]