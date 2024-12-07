FROM python:3.11.11-slim-bookworm

COPY dist/*.whl /

RUN pip install *.whl

EXPOSE 8080

ENTRYPOINT ["python", "-m", "receipt_processor"]
