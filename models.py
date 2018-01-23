class Comment(object):

    def __init__(self, text, date):

        self.text = text
        self.date = date

    def __repr__(self):

        return "email: {}, first_name: {}".format(
            self.text,
            self.date
        )


comment1 = Comment("comment1", "2018-01-01")
comment2 = Comment("comment2", "2018-01-02")
comment3 = Comment("comment3", "2018-01-03")

COMMENTS = [comment1, comment2, comment3]

print COMMENTS

myObj = {"text": "comment1", "Date": "2018-01-01"}
