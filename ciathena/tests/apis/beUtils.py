
def compare_trx_only(expected, actual, tolerance=0.01):
    """
    Compare only TRX column.

    Expected format:
        [date, trx, nrx]

    Actual format:
        [date, trx, nrx]
        OR
        [date, trx]
    """

    if not expected:
        return False, "Expected result is empty"

    if not actual:
        return False, "Actual result is empty"

    if len(expected) != len(actual):
        return False, f"Row count mismatch. Expected {len(expected)}, Got {len(actual)}"

    for i, (exp_row, act_row) in enumerate(zip(expected, actual)):

        if len(exp_row) < 2:
            return False, f"Invalid expected row structure at row {i}"

        expected_date = exp_row[0]
        expected_trx = exp_row[1]  # TRX always index 1 in expected

        if len(act_row) == 3:
            actual_date = act_row[0]
            actual_trx = act_row[1]
        elif len(act_row) == 2:
            actual_date = act_row[0]
            actual_trx = act_row[1]
        else:
            return False, f"Unexpected actual row structure at row {i}"

        if expected_date != actual_date:
            return False, f"Date mismatch at row {i}. Expected {expected_date}, Got {actual_date}"

        if abs(expected_trx - actual_trx) > tolerance:
            return False, f"TRX mismatch at row {i}. Expected {expected_trx}, Got {actual_trx}"

    return True


def compare_nrx_only():
    return None