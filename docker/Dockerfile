FROM python:latest

COPY dist/*.whl /

RUN pip install *.whl

EXPOSE 8080

ENTRYPOINT ["python", "-m", "receipt_processor"]
