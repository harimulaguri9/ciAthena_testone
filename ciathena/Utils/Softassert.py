from playwright.sync_api import expect


class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, condition, message=""):
        """Asserts that a condition is True."""
        try:
            assert condition, message or f"Expected condition to be True, but got {condition}"
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_equal(self, actual, expected, message=""):
        """Asserts that actual == expected."""
        try:
            assert actual == expected, message or f"Expected {expected}, but got {actual}"
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_visible(self, locator, message=""):
        """Asserts that a locator is visible."""
        try:
            expect(locator).to_be_visible()
        except AssertionError as e:
            self.errors.append(message or str(e))

    def assert_text(self, locator, expected_text, message=""):
        """Asserts that locator has expected text."""
        try:
            expect(locator).to_have_text(expected_text)
        except AssertionError as e:
            self.errors.append(message or str(e))

    def assert_all(self):
        """Raises combined AssertionError if any failed."""
        if self.errors:
            raise AssertionError("\nSoft Assertion Failures:\n" + "\n".join(self.errors))
