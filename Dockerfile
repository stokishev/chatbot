FROM python:3.12-slim
WORKDIR /app
COPY ./poetry.lock /app/poetry.lock
RUN PYTHONPATH=/usr/bin/python pip install -r poetry.lock
# COPY ./Writing.py Writing.py
# COPY ./src/project_owl src/project_owl
# COPY ./src/streamlit_google_auth src/streamlit_google_auth
# COPY ./src/reading_comprehension src/reading_comprehension
# COPY ./pages pages

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "sc-chatbot.py","--server.port=8501","--server.address=0.0.0.0"]