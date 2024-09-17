FROM python:3.11

WORKDIR /ecommerce
COPY . .

ENV VIRTUAL_ENV=/ecommerce/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD reflex run --env prod --backend-only