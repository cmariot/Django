# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    elements.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cmariot <cmariot@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/30 13:26:36 by cmariot           #+#    #+#              #
#    Updated: 2024/04/02 10:07:40 by cmariot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='meta',
            tag_type='simple',
            content=content,
            attr=attr
        )


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='img',
            tag_type='simple',
            content=content,
            attr=attr
        )


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='table',
            tag_type='double',
            content=content,
            attr=attr
        )


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='th',
            tag_type='double',
            content=content,
            attr=attr
        )


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='tr',
            tag_type='double',
            content=content,
            attr=attr
        )


class Td(Elem):
    def __init__(self, content=None, attr={}):
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
    def __init__(self, content=None, attr={}):
        super().__init__(
            tag='hr',
            tag_type='simple',
            content=content,
            attr=attr
        )


class Br(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='br', tag_type='simple', content=content, attr=attr)


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
