class TicketList(object):
    def __init__(self, json):
        super().__init__()
        self.json = json

    def get_next(self):
        return self.json['next_page']

    def get_prev(self):
        return self.json['previous_page']

    def display(self):
        output = ""
        for t in self.json['tickets']:
            output += f'\n*Ticket id:{t["id"]}  subject:"{t["raw_subject"]}"\n   priority: "{t["priority"]}"  status: "{t["status"]}" \n'
        if self.get_prev():
            output += '\n type "prev_page" to view previous page'
        if self.get_next():
            output += '\n type "next_page" to view next page'
        return output


class Ticket(object):
    def __init__(self, json):
        super().__init__()
        self.json = json["ticket"]

    def display(self):
        output = ''
        t = self.json
        output += f'\nTicket id:{t["id"]}  subject:"{t["raw_subject"]}"\n priority: "{t["priority"]}"  status: "{t["status"]}" \n \n create at : "{t["created_at"]}" requester_id: "{t["requester_id"]}" \n detail: \n "{t["description"]}" '
        return output
