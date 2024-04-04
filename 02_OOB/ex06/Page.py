from elem import Elem, Text
from elements import (
    Html, Head, Body, Title,
    Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Img, Meta, Hr, Br)


class Page:

    def __init__(self, elem: Elem):
        self.elem = elem

    def is_valid(self) -> bool:

        # It should return True if all the following rules are met,
        # and False otherwise:

        # If during the traversal of the tree, a node is not of type (
        # html, head, body, title, meta, img, table, th, tr, td , ul, ol, li,
        # h1, h2, p, div, span, hr, br or Text, the tree is invalid.

        def traverse_tree(elem, func):
            if not func(elem):
                return False
            if isinstance(elem, Elem):
                for e in elem.content:
                    if not traverse_tree(e, func):
                        return False
            return True

        def check_type(elem):
            return isinstance(elem, (
                Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol,
                Li, H1, H2, P, Div, Span, Hr, Br, Text
            ))

        if not traverse_tree(self.elem, check_type):
            print("An element is not of type (html, head, body, title, " +
                  "meta, img, table, th, tr, td, ul, ol, li, h1, h2, p, div, " +
                  "span, hr, br or Text)")
            return False

        # Html must contain exactly one Head, followed by one Body.

        def check_html_content(elem):
            if isinstance(elem, Html):
                if len(elem.content) != 2:
                    return False
                if not isinstance(elem.content[0], Head):
                    return False
                if not isinstance(elem.content[1], Body):
                    return False
            return True

        if not traverse_tree(self.elem, check_html_content):
            print("Html element must contain exactly one Head, followed" +
                  " by one Body")
            return False

        # Head should only contain a single Title and only that Title.

        def check_head_content(elem):
            if isinstance(elem, Head):
                if len(elem.content) != 1:
                    return False
                if not isinstance(elem.content[0], Title):
                    return False
            return True

        if not traverse_tree(self.elem, check_head_content):
            print("Head should only contain a single Title and only " +
                  "that Title")
            return False

        # Body and Div should only contain elements of the following types:
        # H1, H2, Div, Table, Ul, Ol, Span, or Text.

        def check_div_and_body_content(elem):
            if isinstance(elem, (Body, Div)):
                if len(elem.content) == 0:
                    return True
                for e in elem.content:
                    if not isinstance(
                            e, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                        return False
            return True

        if not traverse_tree(self.elem, check_div_and_body_content):
            print("Body and Div should only contain elements of the " +
                  "following types: H1, H2, Div, Table, Ul, Ol, Span, or Text")
            return False

        # Title, H1, H2, Li, Th, Td should only contain a single Text and
        # only that Text.

        def check_single_text(elem):
            if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
                if len(elem.content) != 1:
                    return False
                if not isinstance(elem.content[0], Text):
                    return False
            return True

        if not traverse_tree(self.elem, check_single_text):
            print("Title, H1, H2, Li, Th, Td should only contain a " +
                  "single Text and only that Text")
            return False

        # P should only contain Text.

        def check_p_content(elem):
            if isinstance(elem, P):
                for e in elem.content:
                    if not isinstance(e, Text):
                        return False
            return True

        if not traverse_tree(self.elem, check_p_content):
            print("P should only contain Text")
            return False

        # Span should only contain Text or P.

        def check_span_content(elem):
            if isinstance(elem, Span):
                for e in elem.content:
                    if not isinstance(e, (Text, P)):
                        return False
            return True

        if not traverse_tree(self.elem, check_span_content):
            print("Span should only contain Text or P")
            return False

        # Ul and Ol should contain at least one Li and only Li.

        def check_ul_and_ol_content(elem):
            if isinstance(elem, (Ul, Ol)):
                if len(elem.content) == 0:
                    return False
                for e in elem.content:
                    if not isinstance(e, Li):
                        return False
            return True

        if not traverse_tree(self.elem, check_ul_and_ol_content):
            print("Ul and Ol should contain at least one Li and only Li")
            return False

        # Tr should contain at least one Th or Td and only Th or Td.
        # Th and Td should be mutually exclusive.

        def check_tr_content(elem):
            if isinstance(elem, Tr):
                if len(elem.content) == 0:
                    return False
                th = False
                td = False
                for e in elem.content:
                    if isinstance(e, Th):
                        if td:
                            return False
                        th = True
                    elif isinstance(e, Td):
                        if th:
                            return False
                        td = True
                    else:
                        return False
            return True

        if not traverse_tree(self.elem, check_tr_content):
            print("Tr should contain at least one Th or Td and only Th " +
                  "or Td. Th and Td should be mutually exclusive")
            return False

        # • Table: should only contain Tr and only Tr.

        def check_table_content(elem):
            if isinstance(elem, Table):
                for e in elem.content:
                    if not isinstance(e, Tr):
                        return False
            return True

        if not traverse_tree(self.elem, check_table_content):
            print("Table should only contain Tr and only Tr")
            return False

        # -> The page is valid.

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


class Page_Tests:

    def test_valid_page(page, function_name):
        if not page.is_valid():
            raise Exception("The page is marked as invalid in " + function_name)

    def test_invalid_page(page, function_name):
        if page.is_valid():
            raise Exception("The page is marked as valid in " + function_name)

    def test_invalid_type_in_tree():
        """
        If during the traversal of the tree, a node is not of type (
        html, head, body, title, meta, img, table, th, tr, td , ul, ol, li,
        h1, h2, p, div, span, hr, br or Text, the tree is invalid.
        """

        # Invalid type in tree
        page = Page(Elem())
        Page_Tests.test_invalid_page(page, "test_invalid_type_in_tree()")

        # Invalid type in tree
        page = Page(Body([Elem()]))
        Page_Tests.test_invalid_page(page, "test_invalid_type_in_tree()")

        # Valid
        page = Page(Html([Head([Title([Text('Hello ground!')])]), Body()]))
        Page_Tests.test_valid_page(page, "test_invalid_type_in_tree()")

    def test_invalid_html():
        """
        Html must contain exactly one Head, followed by one Body.
        """

        # No Head or Body
        page = Page(Html())
        Page_Tests.test_invalid_page(page, "test_invalid_html()")

        # Multiple Head
        page = Page(Html([Head(), Body(), Head()]))
        Page_Tests.test_invalid_page(page, "test_invalid_html()")

        # Body before Head
        page = Page(Html([Body(), Head()]))
        Page_Tests.test_invalid_page(page, "test_invalid_html()")

        # Missing Body
        page = Page(Html([Head()]))
        Page_Tests.test_invalid_page(page, "test_invalid_html()")

        # Missing Head
        page = Page(Html([Body()]))
        Page_Tests.test_invalid_page(page, "test_invalid_html()")

        # Valid
        page = Page(Html([Head([Title([Text('Hello ground!')])]), Body()]))
        Page_Tests.test_valid_page(page, "test_invalid_html()")

    def test_head():
        """
        Head should only contain a single Title and only that Title.
        """

        # Multiple Title
        page = Page(Head([
            Title([Text('Hello ground!')]),
            Title([Text('Hello ground!')])
        ]))
        Page_Tests.test_invalid_page(page, "test_head()")

        # Missing Title
        page = Page(Head([]))
        Page_Tests.test_invalid_page(page, "test_head()")

        # Valid
        page = Page(Head([Title([Text('Hello ground!')])]))
        Page_Tests.test_valid_page(page, "test_head()")

    def test_div_and_body():
        """
        Body and Div should only contain elements of the following types:
        """

        # Invalid type in Body
        page = Page(Body([Title([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_div_and_body()")

        # Invalid type in Div
        page = Page(Div([Title([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_div_and_body()")

        # Valid
        page = Page(
            Body(
                [
                    H1([Text('Hello ground!')]),
                    H2([Text('Hello ground!')]),
                    Div(),
                    Table(),
                    Ul([Li([Text('Hello ground!')])]),
                    Ol([Li([Text('Hello ground!')])]),
                    Span(),
                    Text('Hello ground!'),
                ]
            )
        )
        Page_Tests.test_valid_page(page, "test_div_and_body()")

        page = Page(
            Body(
                [
                    H1([Text('Hello ground!')]),
                    H2([Text('Hello ground!')]),
                    Div(Title([Text('Hello ground!')])),
                    Table(),
                    Ul([Li([Text('Hello ground!')])]),
                    Ol([Li([Text('Hello ground!')])]),
                    Span(),
                    Text('Hello ground!'),
                ]
            )
        )
        Page_Tests.test_invalid_page(page, "test_div_and_body()")

    def test_text():
        """
        Title, H1, H2, Li, Th, Td should only contain a single Text and only that
        Text.
        """

        # Multiple Text in Title
        page = Page(Title([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Multiple Text in H1
        page = Page(H1([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Invalid type in H1
        page = Page(H1([Text('Hello ground!'), Div()]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Multiple Text in Li
        page = Page(Li([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Multiple Text in Th
        page = Page(Th([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Multiple Text in Td
        page = Page(Td([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_invalid_page(page, "test_text()")

        # Valid
        page = Page(Title([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_text()")

        # Valid
        page = Page(H1([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_text()")

        # Valid
        page = Page(Li([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_text()")

        # Valid
        page = Page(Th([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_text()")

        # Valid
        page = Page(Td([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_text()")

    def test_p():
        """
        P should only contain Text.
        """

        # Invalid type in P
        page = Page(P([Text('Hello ground!'), Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_p()")

        # Valid : 1 Text
        page = Page(P([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_p()")

        # Valid : Multiple Text
        page = Page(P([Text('Hello ground!'), Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_p()")

    def test_span():
        """
        Span should only contain Text or P.
        """

        # Invalid type in Span
        page = Page(Span([Text('Hello ground!'), Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_span()")

        # Valid : 1 Text
        page = Page(Span([Text('Hello ground!')]))
        Page_Tests.test_valid_page(page, "test_span()")

        # Valid : Multiple Text
        page = Page(Span([Text('Hello ground!'), P([Text('Hello ground!')])]))
        Page_Tests.test_valid_page(page, "test_span()")

    def test_ul_ol():
        """
        Ul and Ol should contain at least one Li and only Li.
        """

        # Invalid type in Ul
        page = Page(Ul([
            Li([Text('Hello ground!')]),
            Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_ul_ol()")

        # No Li in Ul
        page = Page(Ul())
        Page_Tests.test_invalid_page(page, "test_ul_ol()")

        # Valid : 1 Li
        page = Page(Ol([Li([Text('Hello ground!')])]))
        Page_Tests.test_valid_page(page, "test_ul_ol()")

        # Valid : Multiple Li
        page = Page(Ol([
            Li([Text('Hello ground!')]),
            Li([Text('Hello ground!')])]))
        Page_Tests.test_valid_page(page, "test_ul_ol()")

    def test_tr():
        """
        Tr should contain at least one Th or Td and only Th or Td.
        Th and Td should be mutually exclusive.
        """

        # Invalid type in Tr
        page = Page(Tr([Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_tr()")

        # Non exclusive Th and Td in Tr
        page = Page(Tr([
            Th([Text('Hello ground!')]),
            Td([Text('Hello ground!')])
        ]))
        Page_Tests.test_invalid_page(page, "test_tr()")

        # Valid : only Th
        page = Page(Tr([
            Th([Text('Hello ground!')]),
            Th([Text('Hello ground!')])
        ]))
        Page_Tests.test_valid_page(page, "test_tr()")

        # Valid : only Td
        page = Page(Tr([
            Td([Text('Hello ground!')]),
            Td([Text('Hello ground!')])
        ]))
        Page_Tests.test_valid_page(page, "test_tr()")

        # Invalid type in Tr
        page = Page(
            Tr([Th([Text('Hello ground!')]),
                Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_tr()")

    def test_table():
        """
        Table: should only contain Tr and only Tr.
        """

        # Invalid type in Table
        page = Page(Table([Div([Text('Hello ground!')])]))
        Page_Tests.test_invalid_page(page, "test_table()")

        # Invalid type in Table
        page = Page(Table([
            Tr([Td([Text('Hello ground!')])]),
            Div([Text('Hello ground!')])
        ]))
        Page_Tests.test_invalid_page(page, "test_table()")

        # Valid
        page = Page(Table([Tr([Td([Text('Hello ground!')])])]))
        Page_Tests.test_valid_page(page, "test_table()")


if __name__ == '__main__':

    try:

        list_of_td = [
            Td([Text('Must contain exactly one Head, followed by one Body')]),
            Td([Text('Should only contain a single Title and only that Title')]),
            Td([Text('Should only contain elements of the following types: ' +
                     'H1, H2, Div, Table, Ul, Ol, Span, or Text')]),
            Td([Text('Should only contain a single Text and only that Text')]),
            Td([Text('Should only contain Text')]),
            Td([Text('Should only contain Text')]),
            Td([Text('Should contain at least one Tr and only Tr')]),
            Td([Text('Should contain at least one Th or Td and only Th or Td.' +
                     ' Th and Td should be mutually exclusive')]),
            Td([Text('Should contain at least one Th or Td and only Th or Td.' +
                     ' Th and Td should be mutually exclusive')]),
            Td([Text('Should contain at least one Li and only Li')]),
            Td([Text('Should contain at least one Li and only Li')]),
            Td([Text('Should contain at least one Li and only Li')]),
            Td([Text('Should only contain a single Text and only that Text')]),
            Td([Text('Should only contain a single Text and only that Text')]),
            Td([Text('Should only contain Text')]),
            Td([Text('Should only contain Text')]),
            Td([Text('Should only contain Text or P')]),
            Td([Text('Should only contain Text or P')]),
        ]

        # Example of a valid page with all the elements
        valid_page = Page(
            Html(
                [
                    Head(
                        [
                            Title([Text('Example of a valid page')]
                                  )
                        ]
                    ),
                    Body(
                        [
                            H1([Text(
                                'Example of a valid page with all the elements'
                            )]),
                            H2([Text('Rules of a valid Page:')]),
                            Div([
                                Table(
                                    [
                                        Tr(
                                            [
                                                Th([Text('Html')]),
                                                Th([Text('Head')]),
                                                Th([Text('Body')]),
                                                Th([Text('Title')]),
                                                Th([Text('Meta')]),
                                                Th([Text('Img')]),
                                                Th([Text('Table')]),
                                                Th([Text('Th')]),
                                                Th([Text('Tr')]),
                                                Th([Text('Td')]),
                                                Th([Text('Ul')]),
                                                Th([Text('Ol')]),
                                                Th([Text('Li')]),
                                                Th([Text('H1')]),
                                                Th([Text('H2')]),
                                                Th([Text('P')]),
                                                Th([Text('Div')]),
                                                Th([Text('Span')]),
                                            ],
                                        ),
                                        Tr(
                                            list_of_td
                                        )
                                    ]
                                ),
                            ]),

                            H2([Text('Methods of the Page class:')]),
                            Ul([
                                Li([Text('is_valid()')]),
                                Li([Text('write_to_file()')]),
                            ]),
                            H2([Text('Tests:')]),
                            Ol([
                                Li([Text('test_invalid_type_in_tree')]),
                                Li([Text('test_invalid_html')]),
                                Li([Text('test_head')]),
                                Li([Text('test_div_and_body')]),
                                Li([Text('test_text')]),
                                Li([Text('test_p')]),
                                Li([Text('test_span')]),
                                Li([Text('test_ul_ol')]),
                                Li([Text('test_tr')]),
                                Li([Text('test_table')]),
                            ]),
                            Span([Text('SUCCESS: All tests passed')]),
                        ]
                    )
                ]
            )
        )

        if valid_page.is_valid():
            print(valid_page)
            valid_page.write_to_file('index.html')
        else:
            raise Exception("The valid_page is marked as invalid")

        print("\nTests:\n")
        tests = (
            Page_Tests.test_invalid_type_in_tree,
            Page_Tests.test_invalid_html,
            Page_Tests.test_head,
            Page_Tests.test_div_and_body,
            Page_Tests.test_text,
            Page_Tests.test_p,
            Page_Tests.test_span,
            Page_Tests.test_ul_ol,
            Page_Tests.test_tr,
            Page_Tests.test_table
        )

        for test in tests:
            test()

        print("\nSUCCESS: All tests passed")

    except Exception as e:

        print(e)
