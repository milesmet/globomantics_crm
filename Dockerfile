FROM python:3.7.3-alpine
RUN pip install flask

WORKDIR /src

EXPOSE 5000/tcp

ENTRYPOINT ["python"]
CMD ["start.py"]
