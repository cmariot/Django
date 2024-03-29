#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """

        replace_dict = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            "<": "&lt;",
            ">": "&gt;",
            "§": "&sect;",
            "©": "&copy;",
            "®": "&reg;",
            "à": "&agrave;",
            "è": "&egrave;",
            "é": "&eacute;",
            "ê": "&ecirc;",
            "î": "&icirc;",
            "ô": "&ocirc;",
            "ù": "&ugrave;",
            "û": "&ucirc;",
            "€": "&euro;",
            "\n": "\n<br />\n",
        }

        result = super().__str__()
        for key, value in replace_dict.items():
            result = result.replace(key, value)
        return result


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    [...]

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """

        self.tag = tag
        self.tag_type = tag_type
        self.attr = attr
        self.content = []
        self.level = 0
        if content is not None and self.check_type(content):
            self.add_content(content)

        print(f"tag: {self.tag}")

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

        if self.tag_type == 'double':
            result = '<' + self.tag + self.__make_attr() + '>'
            result += self.__make_content()
            result += '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            result += '<' + self.tag + self.__make_attr() + ' />'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        Example in <img src="hello.jpg">, src="hello.jpg" is an attribute.
        """
        result = str()
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    @staticmethod
    def check_type(content):
        """
        Check the type of the content.
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        content must be a Text, an Elem or a list of Text and Elem.
        """
        if not (
            isinstance(content, Elem) or
            isinstance(content, Text) or
            isinstance(content, list) and all(
                [isinstance(elem, Elem) or isinstance(elem, Text)
                 for elem in content]
            )
        ):
            raise Elem.ValidationError(
                "Content must be a Text, an Elem or a list of Text and Elem."
            )
        return True

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += elem.level * 2 * ' '
            result += elem.__str__() + '\n'
        return result

    def add_content(self, content):
        if type(content) is list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)
        level = self.level
        for elem in self.content:
            elem.level = level
            if elem.tag_type == 'double':
                elem.level += 1

    class ValidationError(Exception):
        """
        A custom exception to manage validation errors.
        """
        def __init__(self, message='Validation error'):
            self.message = message
            super().__init__(self.message)


if __name__ == '__main__':

    try:
        elem = Elem(
                content=Elem(
                    content=Elem(
                        content=Elem()
                        )
                    )
                )
        print(elem)
    except Exception as e:
        print(f"An error occurred: {e}")
