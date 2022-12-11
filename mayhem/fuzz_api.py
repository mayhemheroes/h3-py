#! /usr/bin/python3
import atheris
import sys
import io


with atheris.instrument_imports():
    import h3

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    lat = fdp.ConsumeRegularFloat()
    lng = fdp.ConsumeRegularFloat()
    res = fdp.ConsumeInt(1)
    try:
        h3.latlng_to_cell(lat, lng, res)
        h3.f
    except h3.H3BaseException:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
