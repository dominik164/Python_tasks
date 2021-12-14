import xml.sax

class SaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.fname = ""
        self.lname = ""

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "student":
            print("** Student **")
            lname = attributes["idx"]
            print("Number:", lname)

    def endElement(self, tag):
        if self.current_data == "fname":
            print("First name:", self.fname) 
        elif self.current_data == "lname":
            print("Last name:", self.lname)
        self.current_data = ""

    def characters(self, content):
        if self.current_data == "fname":
            self.fname = content
        elif self.current_data == "lname":
            self.lname = content

if(__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = SaxHandler()
    parser.setContentHandler(handler)
    parser.parse("student.xml")