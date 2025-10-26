# build docker image usong poetry
FROM python:3.12-slim


RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes pip curl
# install packages
RUN pip install poetry uvicorn

# add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# set working directory
WORKDIR /app

# copy poetry.lock and pyproject.toml
COPY poetry.lock pyproject.toml ./

# install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# copy project files
COPY . .

# run application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]