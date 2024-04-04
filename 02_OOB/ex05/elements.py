from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='html',
            tag_type='double',
            content=content,
            attr=attr
        )


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='head',
            tag_type='double',
            content=content,
            attr=attr
        )


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='body',
            tag_type='double',
            content=content,
            attr=attr
        )


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='title',
            tag_type='double',
            content=content,
            attr=attr
        )


class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(
            tag='meta',
            tag_type='simple',
            attr=attr
        )


class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(
            tag='img',
            tag_type='simple',
            attr=attr
        )


class Table(Elem):
    def __init__(
        self,
        content=None,
        attr={'style': 'border-collapse: collapse;'}
    ):
        super().__init__(
            tag='table',
            tag_type='double',
            content=content,
            attr=attr
        )


class Tr(Elem):
    def __init__(
        self,
        content=None,
        attr={}
    ):
        super().__init__(
            tag='tr',
            tag_type='double',
            content=content,
            attr=attr
        )


class Th(Elem):
    def __init__(
        self,
        content=None,
        attr={'style': 'border: 1px solid black;'}
    ):
        super().__init__(
            tag='th',
            tag_type='double',
            content=content,
            attr=attr
        )


class Td(Elem):
    def __init__(
        self,
        content=None,
        attr={'style': 'border: 1px solid black; padding: 5px;'}
    ):
        super().__init__(
            tag='td',
            tag_type='double',
            content=content,
            attr=attr
        )


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='ul',
            tag_type='double',
            content=content,
            attr=attr
        )


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='ol',
            tag_type='double',
            content=content,
            attr=attr
        )


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='li',
            tag_type='double',
            content=content,
            attr=attr
        )


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='h1',
            tag_type='double',
            content=content,
            attr=attr
        )


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='h2',
            tag_type='double',
            content=content,
            attr=attr
        )


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='p',
            tag_type='double',
            content=content,
            attr=attr
        )


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='div',
            tag_type='double',
            content=content,
            attr=attr
        )


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='span',
            tag_type='double',
            content=content,
            attr=attr
        )


class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(
            tag='hr',
            tag_type='simple',
            attr=attr
        )


class Br(Elem):
    def __init__(self, attr=None):
        super().__init__(
            tag='br',
            tag_type='simple',
            attr=attr
        )


def test_default_constructor():

    # Constructor for each class with default values

    classes = (
        Html(),
        Head(),
        Body(),
        Title(),
        Meta(),
        Img(),
        Table(),
        Th(),
        Tr(),
        Td(),
        Ul(),
        Ol(),
        Li(),
        H1(),
        H2(),
        P(),
        Div(),
        Span(),
        Hr(),
        Br()
    )

    print("\n# ----------------------------------------------------------- #\n")

    print('Constructor for each class with default values\n')

    for elem in classes:
        print(elem)

    print("\n# ----------------------------------------------------------- #\n")


def test_default_constructor_with_attr():

    # Constructor for each class with attr

    classes_with_attr = (
        Html(attr={'class': 'html,', 'lang': 'en'}),
        Head(attr={'class': 'head'}),
        Body(attr={'class': 'body'}),
        Title(attr={'class': 'title'}),
        Meta(attr={'class': 'meta'}),
        Img(attr={'class': 'img'}),
        Table(attr={'class': 'table'}),
        Th(attr={'class': 'th'}),
        Tr(attr={'class': 'tr'}),
        Td(attr={'class': 'td'}),
        Ul(attr={'class': 'ul'}),
        Ol(attr={'class': 'ol'}),
        Li(attr={'class': 'li'}),
        H1(attr={'class': 'h1'}),
        H2(attr={'class': 'h2'}),
        P(attr={'class': 'p'}),
        Div(attr={'class': 'div'}),
        Span(attr={'class': 'span'}),
        Hr(attr={'class': 'hr'}),
        Br(attr={'class': 'br'})
    )

    print("\n# ----------------------------------------------------------- #\n")

    print('Constructor for each class with attr\n')

    for elem in classes_with_attr:
        print(elem)

    print("\n# ----------------------------------------------------------- #\n")


def test_default_constructor_with_content():

    # Constructor for each class with content (if applicable)

    classes_with_content = (
        Html(content=[Text('42')]),
        Head(content=[Text('42')]),
        Body(content=[Text('42')]),
        Title(content=[Text('42')]),
        Meta(),
        Img(),
        Table(content=[Text('42')]),
        Th(content=[Text('42')]),
        Tr(content=[Text('42')]),
        Td(content=[Text('42')]),
        Ul(content=[Text('42')]),
        Ol(content=[Text('42')]),
        Li(content=[Text('42')]),
        H1(content=[Text('42')]),
        H2(content=[Text('42')]),
        P(content=[Text('42')]),
        Div(content=[Text('42')]),
        Span(content=[Text('42')]),
        Hr(),
        Br()
    )

    print("\n# ----------------------------------------------------------- #\n")

    print('Constructor for each class with content (if applicable)\n')

    for elem in classes_with_content:
        print(elem)

    print("\n# ----------------------------------------------------------- #\n")


def test_default_constructor_with_content_and_attr():

    classes_with_content_and_attr = (
        Html(content=[Text('42')], attr={'class': 'html'}),
        Head(content=[Text('42')], attr={'class': 'head'}),
        Body(content=[Text('42')], attr={'class': 'body'}),
        Title(content=[Text('42')], attr={'class': 'title'}),
        Meta(attr={'class': 'meta'}),
        Img(attr={'class': 'img'}),
        Table(content=[Text('42')], attr={'class': 'table'}),
        Th(content=[Text('42')], attr={'class': 'th'}),
        Tr(content=[Text('42')], attr={'class': 'tr'}),
        Td(content=[Text('42')], attr={'class': 'td'}),
        Ul(content=[Text('42')], attr={'class': 'ul'}),
        Ol(content=[Text('42')], attr={'class': 'ol'}),
        Li(content=[Text('42')], attr={'class': 'li'}),
        H1(content=[Text('42')], attr={'class': 'h1'}),
        H2(content=[Text('42')], attr={'class': 'h2'}),
        P(content=[Text('42')], attr={'class': 'p'}),
        Div(content=[Text('42')], attr={'class': 'div'}),
        Span(content=[Text('42')], attr={'class': 'span'}),
        Hr(attr={'class': 'hr'}),
        Br(attr={'class': 'br'})
    )

    print("\n# ----------------------------------------------------------- #\n")

    print('Constructor for each class with content and attr\n')

    for elem in classes_with_content_and_attr:
        print(elem)

    print("\n# ----------------------------------------------------------- #\n")


if __name__ == "__main__":

    print(
        Html(
            [
                Head(
                    [
                        Title([Text('Hello ground!')])
                    ]
                ),
                Body(
                    [
                        H1([Text('Oh no, not again!')]),
                        Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
                    ]
                )
            ]
        )
    )

    # test_default_constructor()
    # test_default_constructor_with_attr()
    # test_default_constructor_with_content()
    # test_default_constructor_with_content_and_attr()
