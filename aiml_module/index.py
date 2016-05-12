#encoding=utf8
import web
import aiml
import json
import logging
urls = (
    '/aiml/(.*)', 'AimlProcess'
)

app = web.application(urls, globals())


k = aiml.Kernel()

k.learn("cn-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml cn")

# Loop forever, reading user input from the command
# line and printing responses.

class AimlProcess:
    def GET(self, sentence):
        aimlresponse = k.respond(sentence)
        result = {'sentence':sentence,
                  'response':aimlresponse}
        result = json.dumps(result)
        return result


if __name__ == "__main__":
    app.run()