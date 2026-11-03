FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt fdk_requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Headless Chromium for the Shoonya browser login (FDK_SHOONYA_AUTO_LOGIN). Build with
# --build-arg FDK_BROWSER=0 to skip it (the Telegram-link login still works).
ARG FDK_BROWSER=1
RUN if [ "$FDK_BROWSER" = "1" ]; then apt-get update && apt-get install -y --no-install-recommends chromium chromium-driver && rm -rf /var/lib/apt/lists/*; fi

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
