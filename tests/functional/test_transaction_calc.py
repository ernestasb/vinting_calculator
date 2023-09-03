import contextlib
from io import StringIO
import io
import sys
import pytest

from modules.transaction_calc.main import process_file


@pytest.mark.parametrize(
    "file_content,expected",
    [
        (
            """2015-02-01 S MR
            2015-02-02 S MR
            2015-02-03 L LP
            2015-02-05 S LP
            2015-02-06 S MR
            2015-02-06 L LP
            2015-02-07 L MR
            2015-02-08 M MR
            2015-02-09 L LP
            2015-02-10 L LP
            2015-02-10 S MR
            2015-02-10 S MR
            2015-02-11 L LP
            2015-02-12 M MR
            2015-02-13 M LP
            2015-02-15 S MR
            2015-02-17 L LP
            2015-02-17 S MR
            2015-02-24 L LP
            2015-02-29 CUSPS
            2015-03-01 S MR""",
            """2015-02-01 S MR 1.50 0.50
2015-02-02 S MR 1.50 0.50
2015-02-03 L LP 6.90 -
2015-02-05 S LP 1.50 -
2015-02-06 S MR 1.50 0.50
2015-02-06 L LP 6.90 -
2015-02-07 L MR 4.00 -
2015-02-08 M MR 3.00 -
2015-02-09 L LP 0.00 6.90
2015-02-10 L LP 6.90 -
2015-02-10 S MR 1.50 0.50
2015-02-10 S MR 1.50 0.50
2015-02-11 L LP 6.90 -
2015-02-12 M MR 3.00 -
2015-02-13 M LP 4.90 -
2015-02-15 S MR 1.50 0.50
2015-02-17 L LP 6.90 -
2015-02-17 S MR 1.90 0.10
2015-02-24 L LP 6.90 -
2015-02-29 CUSPS Ignored
2015-03-01 S MR 1.50 0.50
""",
        ),
        (
            """2015-02-01 S MR
            2015-02-02 S MR
            2015-02-03 L LP
            2015-02-05 S LP
            2015-02-06 L MR
            2015-02-06 L LP
            2015-02-07 L MR
            2015-02-08 M MR
            2015-02-09 S LP
            2015-02-10 S LP
            2015-02-10 S MR
            2015-02-10 S MR
            2015-02-10 S MR
            2015-02-10 S MR
            2015-02-10 S MR
            2015-02-11 L LP
            2015-02-12 M MR
            2015-02-13 S LP
            2015-02-15 S MR
            2015-02-17 L LP
            2015-02-17 S MR
            2015-02-24 L LP
            2015-02-29 CUSPS
            2015 CUSPS
            2015-03-01 S S
            2015-03-01 S MR""",
            """2015-02-01 S MR 1.50 0.50
2015-02-02 S MR 1.50 0.50
2015-02-03 L LP 6.90 -
2015-02-05 S LP 1.50 -
2015-02-06 L MR 4.00 -
2015-02-06 L LP 6.90 -
2015-02-07 L MR 4.00 -
2015-02-08 M MR 3.00 -
2015-02-09 S LP 1.50 -
2015-02-10 S LP 1.50 -
2015-02-10 S MR 1.50 0.50
2015-02-10 S MR 1.50 0.50
2015-02-10 S MR 1.50 0.50
2015-02-10 S MR 1.50 0.50
2015-02-10 S MR 1.50 0.50
2015-02-11 L LP 0.40 6.50
2015-02-12 M MR 3.00 -
2015-02-13 S LP 1.50 -
2015-02-15 S MR 2.00 -
2015-02-17 L LP 6.90 -
2015-02-17 S MR 2.00 -
2015-02-24 L LP 6.90 -
2015-02-29 CUSPS Ignored
2015 CUSPS Ignored
2015-03-01 S S Ignored
2015-03-01 S MR 1.50 0.50
""",
        ),
    ],
)
def test_transaction_calc(tmp_path, file_content, expected, default_config):
    data_path = tmp_path / "transactions.txt"
    # write data to file
    with open(data_path, "w") as file:
        file.write(file_content)
    # catch stdout
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        process_file(data_path, default_config)

    print(output.getvalue())
    assert expected == output.getvalue()
