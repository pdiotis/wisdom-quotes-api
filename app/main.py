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
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
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
    {"author": "Ralph Waldo Emerson", "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us."}
]
motivational_quotes = [
    {"author": "Winston Churchill", "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts."},
    {"author": "Winston Churchill", "quote": "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty."},
    {"author": "Seneca", "quote": "Every new beginning comes from some other beginning's end."},
    {"author": "Albert Einstein", "quote": "A person who never made a mistake never tried anything new."},
    {"author": "Maya Angelou", "quote": "If you don't like something, change it. If you can't change it, change your attitude."},
    {"author": "Ralph Waldo Emerson", "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us."},
    {"author": "Thomas A. Edison", "quote": "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time."},
    {"author": "Vince Lombardi", "quote": "The price of success is hard work, dedication to the job at hand, and the determination that whether we win or lose, we have applied the best of ourselves to the task at hand."},
    {"author": "Eleanor Roosevelt", "quote": "The future belongs to those who believe in the beauty of their dreams."},
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
    {"author": "Confucius", "quote": "Our greatest glory is not in never falling, but in rising every time we fall."},
    {"author": "Bruce Lee", "quote": "A goal is not always meant to be reached, it often serves simply as something to aim at."},
    {"author": "Bruce Lee", "quote": "Do not pray for an easy life, pray for the strength to endure a difficult one."},
    {"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."},
    {"author": "Steve Jobs", "quote": "Stay hungry, stay foolish."},
    {"author": "Jim Rohn", "quote": "You are the average of the five people you spend the most time with."},
    {"author": "Jim Rohn", "quote": "Discipline is the bridge between goals and accomplishment."},
    {"author": "Les Brown", "quote": "The moment you give up, is the moment you let someone else win."},
    {"author": "Les Brown", "quote": "You don't have to be great to start, but you have to start to be great."},
    {"author": "Nelson Mandela", "quote": "It always seems impossible until it's done."},
    {"author": "Franklin D. Roosevelt", "quote": "The only thing we have to fear is fear itself."},
    {"author": "Dalai Lama", "quote": "The purpose of our lives is to be happy."},
    {"author": "Dalai Lama", "quote": "In order to carry a positive action we must develop here a positive vision."},
    {"author": "Mahatma Gandhi", "quote": "The future depends on what you do today."},
    {"author": "Mahatma Gandhi", "quote": "Be the change that you wish to see in the world."},
    {"author": "Oscar Wilde", "quote": "We are all in the gutter, but some of us are looking at the stars."},
    {"author": "John Lennon", "quote": "Life is what happens when you are busy making other plans."},
    {"author": "Zig Ziglar", "quote": "Your attitude, not your aptitude, will determine your altitude."},
    {"author": "Vince Lombardi", "quote": "Perfection is not attainable, but if we chase perfection we can catch excellence."},
    {"author": "Eleanor Roosevelt", "quote": "No one can make you feel inferior without your consent."}
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

@app.get("/motivation")
def get_quote():
    return random.choice(motivational_quotes)
