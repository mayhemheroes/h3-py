# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

# Install dependencies

ADD . /src
WORKDIR /src
RUN python3 -m pip3 install 'h3==4.0.0b2'

CMD ["/src/mayhem/fuzz_api.py"]