FROM hseling/hseling-api-base:python3.6-alpine3.7 as build

LABEL maintainer="Oleg Serikov <info@linghub.ru>"

RUN mkdir /dependencies
COPY ./hseling_api_fake_corpora_interface/requirements.txt /dependencies/requirements.txt
COPY ./hseling_api_fake_corpora_interface/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=build /dependencies /dependencies

COPY ./hseling_lib_fake_corpora_interface /dependencies/hseling_lib_fake_corpora_interface
RUN pip install /dependencies/hseling_lib_fake_corpora_interface

COPY ./hseling_api_fake_corpora_interface/hseling_api_fake_corpora_interface /app/hseling_api_fake_corpora_interface
COPY ./hseling_api_fake_corpora_interface/main.py /app/main.py

ENV HSELING_API_FAKE_CORPORA_INTERFACE_SETTINGS="/app/hseling_api_fake_corpora_interface/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost/healthz || exit 1
