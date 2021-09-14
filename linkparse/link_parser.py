class LinkParserResult:
    uri: str = ""

    relationship: str = ""

    link_type: str = ""

    datetime: str = ""

    title: str = ""

    link_from: str = ""

    link_until: str = ""

    def __init__(self, uri: str = "",
                 relationship: str = "",
                 link_type: str = "",
                 datetime: str = "",
                 title: str = "",
                 link_from: str = "",
                 link_until: str = ""):
        self.uri = uri.strip()
        self.relationship = relationship
        self.datetime = datetime
        self.link_type = link_type
        self.title = title
        self.link_from = link_from
        self.link_until = link_until


class LinkParser:

    def parse(self, link_header: str) -> list[LinkParserResult]:
        """
        Parses given link header string into link parser results.

        :param link_header: link header as string.
        :return: List containing link parser results.
        """
        pass
