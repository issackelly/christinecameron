from django.http import HttpResponseRedirect

class NoWWW:
    def process_request(self, request):
        if request.get_host() != "christineandcameron.com":
            return HttpResponseRedirect("http://christineandcameron.com%s" % request.get_full_path())

        if request.get_full_path() == "/favicon.ico":
            return HttpResponseRedirect("/static/img/favicon.ico")
