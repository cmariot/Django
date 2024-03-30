from elem import Elem, Text
from elements import (
    Html, Head, Body, Title,
    Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span)


class Page:

    def __init__(self, elem: Elem):
        self.elem = elem

    def is_valid(self) -> bool:

        # It should return True if all the following rules are met,
        # and False otherwise:

        # If during the traversal of the tree, a node is not of type (
        # html, head, body, title, meta, img, table, th, tr, td , ul, ol, li,
        # h1, h2, p, div, span, hr, br or Text, the tree is invalid.

        if not isinstance(self.elem, (Elem, Text)):
            print("Error: Invalid element type")
            return False
        try:
            self.elem.check_type(self.elem.content)
        except Elem.ValidationError:
            print("Error: Invalid element type")
            return False

        # Html must contain exactly one Head, followed by one Body.

        if not isinstance(self.elem, Html):
            print("Error: Html element not found")
            return False
        elif len(self.elem.content) != 2:
            print("Error: Html element must contain exactly 2 elements")
            return False
        elif (not isinstance(self.elem.content[0], Head) or
              not isinstance(self.elem.content[1], Body)):
            print("Error: Html element must contain a Head and a Body")
            return False

        head = self.elem.content[0]
        body = self.elem.content[1]

        # Head should only contain a single Title and only that Title.

        if len(head.content) != 1:
            print("Error: Head element must contain exactly 1 element")
            return False
        elif not isinstance(head.content[0], Title):
            print("Error: Head element must contain a Title")
            return False

        # Body and Div should only contain elements of the following types:
        # H1, H2, Div, Table, Ul, Ol, Span, or Text.

        def check_body_content(content):
            for elem in content:
                if isinstance(elem, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                    if isinstance(elem, Div):
                        return check_body_content(elem.content)
                else:
                    return False
            return True

        if not check_body_content(body.content):
            print(
                "Error: Body and Div elements must contain only H1, H2, Div, " +
                "Table, Ul, Ol, Span, or Text elements"
            )
            return False

        # Title, H1, H2, Li, Th, Td should only contain a single Text and
        # only that Text.

        def check_single_text(elem):
            if len(elem.content) != 1:
                return False
            elif not isinstance(elem.content[0], Text):
                return False
            return True

        def check_single_text_content(content):
            for elem in content:
                if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
                    if not check_single_text(elem):
                        return False
                elif not isinstance(elem, Text):
                    if not check_single_text_content(elem.content):
                        return False
            return True

        if not check_single_text_content(self.elem.content):
            print(
                "Error: Title, H1, H2, Li, Th, Td elements must contain only" +
                " one Text element"
            )
            return False

        # P should only contain Text.

        def check_p_content(content):
            for elem in content:
                if isinstance(elem, P):
                    if not all(isinstance(e, Text) for e in elem.content):
                        return False
                elif not isinstance(elem, Text):
                    if not check_p_content(elem.content):
                        return False
            return True

        if not check_p_content(body.content):
            print("Error: P elements must contain only Text elements")
            return False

        # Span should only contain Text or P.

        def check_span_content(content):
            for elem in content:
                if isinstance(elem, Span):
                    if not all(isinstance(e, (Text, P)) for e in elem.content):
                        return False
                elif not isinstance(elem, (Text, P)):
                    if not check_span_content(elem.content):
                        return False
            return True

        if not check_span_content(body.content):
            print("Error: Span elements must contain only Text or P elements")
            return False

        # Ul and Ol should contain at least one Li and only Li.
        def check_ul_ol_content(content):
            for elem in content:
                if isinstance(elem, (Ul, Ol)):
                    if not any(isinstance(e, Li) for e in elem.content):
                        return False
                    if not all(isinstance(e, Li) for e in elem.content):
                        return False
                elif not isinstance(elem, (Li, Text)):
                    if not check_ul_ol_content(elem.content):
                        return False
            return True

        if not check_ul_ol_content(body.content):
            print(
                "Error: Ul and Ol elements must contain at least one Li element"
            )
            return False

        # Tr should contain at least one Th or Td and only Th or Td. Th and
        # Td should be mutually exclusive.

        def check_tr_content(content):
            for elem in content:
                if isinstance(elem, Tr):
                    if not any(isinstance(e, (Th, Td)) for e in elem.content):
                        return False
                    if not all(isinstance(e, (Th, Td)) for e in elem.content):
                        return False
                elif not isinstance(elem, (Th, Td, Text)):
                    if not check_tr_content(elem.content):
                        return False
            return True

        if not check_tr_content(body.content):
            print(
                "Error: Tr elements must contain at least one Th or Td element"
            )
            return False

        # • Table: should only contain Tr and only Tr.

        def check_table_content(content):
            for elem in content:
                if isinstance(elem, Table):
                    if not all(isinstance(e, Tr) for e in elem.content):
                        return False
                elif not isinstance(elem, (Tr, Text)):
                    if not check_table_content(elem.content):
                        return False
            return True

        if not check_table_content(body.content):
            print("Error: Table elements must contain only Tr elements")
            return False

        return True

    def __str__(self) -> str:

        # if the first element is an instance of Html
        if isinstance(self.elem, Html):
            doctype = '<!DOCTYPE html>\n'
            return doctype + str(self.elem)

        # else
        return str(self.elem)

    def write_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            file.write(str(self))


if __name__ == '__main__':

    try:

        page = Page(
            Html(
                [
                    Head(
                        [
                            Title([Text('Hello ground!')]),
                        ]
                    ),
                    Body(
                        [
                            H1([Text('Oh no, not again!')]),
                            Div(
                                [
                                    Div()
                                ]
                            )

                        ]
                    )
                ]
            )
        )

        print(page.is_valid())
        print(page)
        page.write_to_file('test.html')

    except Exception as e:

        print(e)
