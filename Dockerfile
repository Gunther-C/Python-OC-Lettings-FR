FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["waitress-serve", "--port=8000", "oc_lettings_site.wsgi:application"]
