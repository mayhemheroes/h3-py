# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

## Install build dependencies.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y clang cmake make ninja-build

# Install dependencies
ADD . /src
WORKDIR /src
ENV CC="/usr/bin/clang"
ENV CFLAGS="-fsanitize=fuzzer-no-link,undefined"
ENV CXX="/usr/bin/clang++"
ENV CXXFLAGS="-fsanitize=fuzzer-no-link,undefined"
RUN pip3 install .

ENV LD_PRELOAD="${LD_PRELOAD}:/usr/local/lib/python3.9/dist-packages/ubsan_with_fuzzer.so"
CMD ["/src/mayhem/fuzz_api.py"]