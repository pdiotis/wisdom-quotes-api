from fastapi import FastAPI
import random
import os

app = FastAPI(
    title="Wisdom Quotes API",
    version=os.getenv("APP_VERSION", "0.1.0")
)

quotes = [
    {"author": "Socrates", "quote": "To know, is to know that you know nothing. That is the meaning of true knowledge."},
    {"author": "Aristotle", "quote": "Educating the mind without educating the heart is no education at all."},
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance you must keep moving."},
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."}
    {"author": "Plato", "quote": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light."},
    {"author": "Confucius", "quote": "Our greatest glory is not in never falling, but in rising every time we fall."},
    {"author": "Lao Tzu", "quote": "The journey of a thousand miles begins with a single step."},
    {"author": "Leonardo da Vinci", "quote": "Learning never exhausts the mind."},
    {"author": "Mahatma Gandhi", "quote": "Be the change that you wish to see in the world."},
    {"author": "Martin Luther King Jr.", "quote": "The time is always right to do what is right."},
    {"author": "Maya Angelou", "quote": "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel."},
    {"author": "Oscar Wilde", "quote": "Be yourself; everyone else is already taken."},
    {"author": "Marie Curie", "quote": "Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less."},
    {"author": "Friedrich Nietzsche", "quote": "He who has a why to live for can bear almost any how."},
    {"author": "Helen Keller", "quote": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart."},
    {"author": "Seneca", "quote": "Every new beginning comes from some other beginning's end."},
    {"author": "Ralph Waldo Emerson", "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us."},
]

@app.get("/")
def root():
    return {"message": "Welcome to a demo Wisdom Quotes API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": app.version}

@app.get("/quote")
def get_quote():
    return random.choice(quotes)
