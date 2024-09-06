FROM python:3.10

WORKDIR /workspace

COPY requirements.txt .  # Make sure the requirements.txt is copied to the right directory
RUN pip install --upgrade pip && pip install -r requirements.txt
