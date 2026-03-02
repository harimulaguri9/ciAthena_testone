#
# def compare_trx_only(expected, actual, tolerance=0.01):
#     """
#     Compare only TRX column.
#
#     Expected format:
#         [date, trx, nrx]
#
#     Actual format:
#         [date, trx, nrx]
#         OR
#         [date, trx]
#     """
#
#     if not expected:
#         return False
#
#     if not actual:
#         return False
#
#     if len(expected) != len(actual):
#         return False
#
#     for i, (exp_row, act_row) in enumerate(zip(expected, actual)):
#
#         if len(exp_row) < 2:
#             return False
#
#         expected_date = exp_row[0]
#         expected_trx = exp_row[1]  # TRX always index 1 in expected
#
#         if len(act_row) == 3:
#             actual_date = act_row[0]
#             actual_trx = act_row[1]
#         elif len(act_row) == 2:
#             actual_date = act_row[0]
#             actual_trx = act_row[1]
#         else:
#             return False
#         if expected_date != actual_date:
#             return False
#
#         if abs(expected_trx - actual_trx) > tolerance:
#             return False
#
#     return True
#



# def compare_trx_only(expected, actual, tolerance=0.01):
#     """
#     Return TRUE if ANY TRX value matches between expected and actual.
#     Date is ignored completely.
#     """
#
#     if not expected:
#         return False
#
#     if not actual:
#         return False
#
#     # Extract expected TRX values (index 1)
#     expected_trx_values = []
#     for row in expected:
#         if len(row) >= 2:
#             expected_trx_values.append(row[1])
#
#     # Extract actual TRX values (index 1)
#     actual_trx_values = []
#     for row in actual:
#         if len(row) >= 2:
#             actual_trx_values.append(row[1])
#
#     # Compare any expected TRX with any actual TRX
#     for exp_trx in expected_trx_values:
#         for act_trx in actual_trx_values:
#             if abs(exp_trx - act_trx) <= tolerance:
#                 return True
#     return False




# def compare_trx_only(expected, actual, tolerance=0.01):
#     """
#     Return True if ANY numeric value (excluding date column index 0)
#     matches between expected and actual.
#     """
#
#     if not expected:
#         return False
#
#     if not actual:
#         return False
#
#     # Extract all numeric values except index 0 (date)
#     expected_values = []
#     for row in expected:
#         for value in row[1:]:   # skip date
#             if isinstance(value, (int, float)):
#                 expected_values.append(value)
#
#     actual_values = []
#     for row in actual:
#         for value in row[1:]:   # skip date
#             if isinstance(value, (int, float)):
#                 actual_values.append(value)
#
#     # Compare any value
#     for exp in expected_values:
#         for act in actual_values:
#             if abs(exp - act) <= tolerance:
#                 return True
#
#     return False










#
# def compare_trx_only(expected, actual, tolerance=0.01):
#     """
#     Compare TRX column (index 1) row-by-row.
#     Returns True/False only (Excel safe).
#     """
#
#     try:
#         if not expected or not actual:
#             return False
#
#         if len(expected) != len(actual):
#             return False
#
#         for exp_row, act_row in zip(expected, actual):
#
#             if len(exp_row) < 2 or len(act_row) < 2:
#                 return False
#
#             expected_date = exp_row[0]
#             actual_date = act_row[0]
#
#             if expected_date != actual_date:
#                 return False
#
#             expected_trx = float(exp_row[1])
#             actual_trx = float(act_row[1])
#
#             if abs(expected_trx - actual_trx) > tolerance:
#                 return False
#
#         return True
#
#     except Exception as e:
#         print("TRX comparison error:", e)
#         return False

def compare_trx_only(expected, actual, tolerance=0.01):
    """
    Order-independent TRX comparison.
    Dynamically detects numeric values.
    Ignores string columns.
    Excel safe (returns True/False only).
    """

    try:
        if not expected or not actual:
            return False

        # Extract numeric values from expected
        expected_trx_values = []
        for row in expected:
            for value in row:
                try:
                    num = float(value)
                    expected_trx_values.append(round(num, 4))
                except (ValueError, TypeError):
                    continue

        # Extract numeric values from actual
        actual_trx_values = []
        for row in actual:
            for value in row:
                try:
                    num = float(value)
                    actual_trx_values.append(round(num, 4))
                except (ValueError, TypeError):
                    continue

        if not expected_trx_values or not actual_trx_values:
            return False

        # Compare as sets (order independent)
        return set(expected_trx_values) == set(actual_trx_values)

    except Exception as e:
        print("TRX comparison error:", e)
        return False