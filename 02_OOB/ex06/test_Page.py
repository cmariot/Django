import unittest
from Page import Page, Html, Head, Body, Title, H1, H2, Div, Table, Ul, Ol, Span, Text, P, Li, Th, Td, Tr

class PageTest(unittest.TestCase):

    def test_is_valid_invalid_element_type(self):
        page = Page(elem=123)  # Invalid element type
        self.assertFalse(page.is_valid())

    def test_is_valid_html_element_not_found(self):
        page = Page(elem=Body())  # Html element not found
        self.assertFalse(page.is_valid())

    def test_is_valid_html_element_content_length(self):
        page = Page(elem=Html(content=[Head(), Body(), Div()]))  # Html element must contain exactly 2 elements
        self.assertFalse(page.is_valid())

    def test_is_valid_html_element_content_types(self):
        page = Page(elem=Html(content=[Body(), Head()]))  # Html element must contain a Head and a Body
        self.assertFalse(page.is_valid())

    def test_is_valid_head_element_content_length(self):
        page = Page(elem=Html(content=[Head(content=[Title(), Title()]), Body()]))  # Head element must contain exactly 1 element
        self.assertFalse(page.is_valid())

    def test_is_valid_head_element_content_type(self):
        page = Page(elem=Html(content=[Head(content=[Div()]), Body()]))  # Head element must contain a Title
        self.assertFalse(page.is_valid())

    def test_is_valid_body_and_div_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[H1(), H2(), Div(content=[Table(), Ul(), Ol(), Span(), Text(), P(), Li(), Th(), Td(), Tr()])])]))  # Body and Div elements must contain only H1, H2, Div, Table, Ul, Ol, Span, or Text elements
        self.assertFalse(page.is_valid())

    def test_is_valid_title_h1_h2_li_th_td_element_content_length(self):
        page = Page(elem=Html(content=[Head(content=[Title(content=[Text(), Text()])]), Body()]))  # Title, H1, H2, Li, Th, Td elements must contain only one Text element
        self.assertFalse(page.is_valid())

    def test_is_valid_p_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[P(content=[Text(), Div()])])]))  # P elements must contain only Text elements
        self.assertFalse(page.is_valid())

    def test_is_valid_span_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[Span(content=[Text(), P(), Div()])])]))  # Span elements must contain only Text or P elements
        self.assertFalse(page.is_valid())

    def test_is_valid_ul_ol_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[Ul(content=[Li(), Text()]), Ol(content=[Li(), Text(), Div()])])]))  # Ul and Ol elements must contain at least one Li element
        self.assertFalse(page.is_valid())

    def test_is_valid_tr_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[Table(content=[Tr(content=[Th(), Td(), Text()])])])]))  # Tr elements must contain at least one Th or Td element
        self.assertFalse(page.is_valid())

    def test_is_valid_table_element_content_types(self):
        page = Page(elem=Html(content=[Head(content=[Title()]), Body(content=[Table(content=[Tr(content=[Th(), Td(), Text()]), Div()])])]))  # Table elements must contain only Tr elements
        self.assertFalse(page.is_valid())

    def test_is_valid_valid_page(self):
        page = Page(elem=Html(content=[Head(content=[Title(content=[Text()])]), Body(content=[H1(content=[Text()]), Div(content=[Table(content=[Tr(content=[Th(content=[Text()])])])])])]))  # Valid page
        self.assertTrue(page.is_valid())

if __name__ == '__main__':
    unittest.main()