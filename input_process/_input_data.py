import pathlib
import attr


def _to_path(item):
    return pathlib.Path(item)


def _is_existing_file(instance, attrib, value: pathlib.Path):
    return value.is_file()


@attr.s
class InputData:

    actual_period_sales = attr.ib(type=pathlib.Path, converter=_to_path)

