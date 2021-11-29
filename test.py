import io
import unittest
import unittest.mock
from tickets import Ticket
from main import CommandShell


class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.shell = CommandShell

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_ticket(self, command, expected_output, mock_stdout):
        self.shell.do_ticket(command, "")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_ticket_input_str(self):
        self.shell.do_ticket("sdf", 'please enter number for ticket id\n')

        self.shell.do_ticket("1", 'please enter number for ticket id\n')


if __name__ == '__main__':
    unittest.main()
