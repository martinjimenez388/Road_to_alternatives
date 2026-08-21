FROM python:3.13.5-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy

COPY customer.py model_LogReg_CourseLeadScoring.bin ./

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "--port=9696", "customer:app"]