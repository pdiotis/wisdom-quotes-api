# get the official python image
FROM python:3.11-slim

# working directory inside the container
WORKDIR /app

# copy  requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy all the project inside the container
COPY . .

ARG APP_VERSION=0.1.1
ENV APP_VERSION=${APP_VERSION}

# start command (runs FastAPI with  Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
