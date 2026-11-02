import io
import unittest
from contextlib import redirect_stdout
from lantern import print_tasks
class EmptyListTest(unittest.TestCase):
    def test_empty_list_message(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            print_tasks([])
        self.assertIn("No tasks", buf.getvalue())
if __name__ == "__main__":
    unittest.main()