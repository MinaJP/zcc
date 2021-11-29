
import os
import cmd
from decouple import config, UndefinedValueError
from tickets import TicketList, Ticket
from request import *


class CommandShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.cur = None
    user = config("EMAIL").split('@')[0]
    prompt = f'({user})$ '
    intro = f'Welcome to ticket viewer.\n You are login with email {config("EMAIL")} on "{config("DOMAIN")}.zendesk.com" \n type "help" to view list of commands \n type "list" to view list of tickets \n type "ticket |id|" to view ticket detail'

    def do_list(self, arg):
        'provide list of 25 tickets'
        if self.cur is None:
            success, output = get_tickets(
                f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets.json?per_page=25')
            if success:
                self.cur = TicketList(output)
            else:
                print(output)
                return True
        print(self.cur.display())
        list()

    def do_ticket(self, arg):
        'view detail of the ticket with id provided. Example command "ticket 1" '
        id = None
        try:
            id = int(arg)
            success, output = get_tickets(
                f'https://{config("DOMAIN")}.zendesk.com/api/v2/tickets/{id}.json')
            if success:
                ticket = Ticket(output)
                print(ticket.display())
            else:
                print(output)

        except:
            print("please enter number for ticket id")

    def do_next_page(self, arg):
        'go to next page of ticket'
        if not self.cur:
            self.do_list('')

        elif not self.cur.get_next():
            print("this is the last page")
        else:
            success, output = get_tickets(self.cur.get_next()
                                          )
            if success:
                self.cur = TicketList(output)
                self.do_list('')
            else:
                print(output)

    def do_prev_page(self, arg):
        'go to previous page of ticket'
        if not self.cur:
            self.do_list('')

        elif not self.cur.get_prev():
            print("this is the first page")
        else:
            success, output = get_tickets(self.cur.get_prev()
                                          )
            if success:
                self.cur = TicketList(output)
                self.do_list('')
            else:
                print(output)

    def do_quit(self, arg):
        'quit the ticket viewer'
        print('Thank you for using ticket viewer')
        quit()
        return True


def main():
    """ Main entry point of the app """
    try:
        # check configuration
        config("EMAIL")
        config("DOMAIN")
        config("PASSWORD")
        CommandShell().cmdloop()
    except UndefinedValueError as e:
        print("please set up .env file properly")
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
    # CommandShell().cmdloop()
