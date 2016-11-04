import os

import webapp2

INDEX_PAGE_PATH = 'index.html'


def read_html(path):
    with open(path, 'r') as f:
        return f.read()


class PageHandler(webapp2.RequestHandler):
    def get(self, page):
        if not page:
            page = INDEX_PAGE_PATH

        page_path = os.path.join(os.path.dirname(__file__), page)

        if not os.path.isfile(page_path):
            webapp2.abort(404)

        self.response.write(read_html(page_path))


app = webapp2.WSGIApplication([
    ('/(.*\.html)?', PageHandler)
], debug=False)
