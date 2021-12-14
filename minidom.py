import xml.dom.minidom


if(__name__ == "__main__"):
    xml_file = xml.dom.minidom.parse("student.xml")
    students = xml_file.getElementsByTagName("student")

    f_name = students[0].getElementsByTagName("fname")[0].firstChild.data

    students[0].getElementsByTagName("fname")[0].firstChild.data = "Alek"

    with open("students.xml", "w") as xml_file_new:
        xml_file_new.write(xml_file.toxml())