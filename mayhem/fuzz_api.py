#! /usr/bin/env python3
import atheris
import sys

with atheris.instrument_imports():
    import h3


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    iteration_test = fdp.ConsumeIntInRange(0, 13)

    try:
        h = h3.latlng_to_cell(fdp.ConsumeFloat(), fdp.ConsumeFloat(), fdp.ConsumeIntInRange(0, 15))
        if iteration_test == 0:
            h3.cell_to_latlng(h)
        elif iteration_test == 2:
            h3.cell_to_parent(h, fdp.ConsumeIntInRange(0, 15))
        elif iteration_test == 3:
            h3.cell_to_children(h, fdp.ConsumeIntInRange(0, 15))
        elif iteration_test == 4:
            h3.get_resolution(h)
        elif iteration_test == 5:
            h3.is_valid_cell(h)
        elif iteration_test == 6:
            h3.is_pentagon(h)
        elif iteration_test == 7:
            h3.get_base_cell_number(h)
        elif iteration_test == 8:
            h3.get_icosahedron_faces(h)
        elif iteration_test == 9:
            h3.cell_area(h)
        elif iteration_test == 10:
            h3.edge_length(h)
        elif iteration_test == 11:
            h3.average_hexagon_area(fdp.ConsumeIntInRange(0, 15))
        elif iteration_test == 12:
            h3.average_hexagon_edge_length(fdp.ConsumeIntInRange(0, 15))
        elif iteration_test == 13:
            h3.grid_ring(h, fdp.ConsumeIntInRange(0, 15))
    except h3.H3BaseException:
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
