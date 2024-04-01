import unittest
from Page import Page
from elements import (Html, Head, Body, Title, P, Div, Span, Text,
                      Ul, Ol, Li, Table, Tr, Th, Td, H1)


class TestPage(unittest.TestCase):

    def test_valid_page(self):
        # Create a valid page
        elem = Html([
            Head([Title(Text("Page Title"))]),
            Body([
                H1(Text("Heading 1")),
                Div([
                    Span([Text("Span Text")]),
                ]),
                Span([Text("Span Text")]),
                Ul([Li(Text("List Item 1")), Li(Text("List Item 2"))]),
                Ol([Li(Text("List Item 1")), Li(Text("List Item 2"))]),
                Table([
                    Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
                    Tr([Td(Text("Cell 1")), Td(Text("Cell 2"))])
                ])
            ])
        ])
        page = Page(elem)
        self.assertTrue(page.is_valid())

    def test_invalid_page(self):
        # Create an invalid page
        elem = Html([
            Head([Title(Text("Page Title"))]),
            Body([
                H1(Text("Heading 1")),
                Div([
                    P(Text("Paragraph 1")),
                    P(Text("Paragraph 2"))
                ]),
                Span([Text("Span Text")]),
                Ul([Li(Text("List Item 1")), Li(Text("List Item 2"))]),
                Ol([Li(Text("List Item 1")), Li(Text("List Item 2"))]),
                Table([
                    Tr([Th(Text("Header 1")), Td(Text("Cell 2"))]),
                    # Invalid: Th and Td not mutually exclusive
                    Tr([Td(Text("Cell 1")), Td(Text("Cell 2"))])
                ])
            ])
        ])
        page = Page(elem)
        self.assertFalse(page.is_valid())


if __name__ == '__main__':
    unittest.main()
