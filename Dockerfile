From python:3.8-alpine
WORKDIR /home/app/
COPY tfidf tfidf
COPY article.txt article.txt
ENTRYPOINT ["python", "-m", "tfidf", "-f", "article.txt", "-t", "database"]