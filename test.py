import io
import unittest
import unittest.mock
from tickets import Ticket, TicketList
from main import CommandShell
from request import get_tickets
from decouple import config


class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.shell = CommandShell()
        self.shell.do_list("")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_ticket(self, command, expected_output, mock_stdout):
        self.shell.do_ticket(command)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_prev(self, command, expected_output, mock_stdout):
        self.shell.do_prev_page("")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_request(self):
        success, result = get_tickets(
            f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets')
        self.assertTrue(success)
        self.assertTrue(isinstance(result, dict))

    def test_request_invalid_user(self):
        success, result = get_tickets(
            f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets', auth=('user', 'pass'))
        self.assertFalse(success)

    def test_ticket_input_str(self):
        self.assert_stdout_ticket("sdf", 'please enter number for ticket id\n')

    def test_pagination(self):
        success, result = get_tickets(
            f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets/count.json')
        count = result['count']['value']
        if count > 25:
            success, json = get_tickets(
                f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets')
            tl = TicketList(json)
            self.assertTrue(tl.get_next is not None)
            self.assertFalse(tl.get_prev is None)

    def test_prev_page(self):
        self.assert_stdout_prev("", 'this is the first page\n')


if __name__ == '__main__':
    unittest.main()
