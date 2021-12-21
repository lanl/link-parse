from linkparse.errors import ParseError
from linkparse.link_parser import LinkParser, LinkParserResult


class AggregatorLinkParser(LinkParser):
    """

    Python version of the character based link-header parser used in the aggregator. Original version written in Java.

    State Machine based link parser parses the link header character by character (character based state transitions).
    Used in the initial implementation of memento validator.

    Original dictionary based result transformed into linkparser library return formats.

    Author: Luda Balakirawa (ludab@lanl.gov)

    """
    _curr = 0

    def parse(self, link_header: str) -> list[LinkParserResult]:
        """
        Parses given link header string into link parser results.

        :param link_header: link header as string.
        :return: List containing link parser results.
        :raise ParseError: ParserError
        """
        self._curr = 0
        href = None
        attributes = dict()
        results = []

        while self._curr < len(link_header):

            c = link_header[self._curr]

            if c == "<":
                if href is not None:
                    raise ParseError()
                else:
                    href = self._parse_link(link_header)
            elif c == ';' or c == ' ' or c == '\n' or c == '\r':
                self._curr = self._curr + 1
                continue
            elif c == ",":
                results.append(self._transform(href, attributes))
                attributes = dict()
                href = None
                self._curr = self._curr + 1
            else:
                key, value = self._parse_attributes(link_header)
                attributes[key] = value

        return results

    def _parse_link(self, link_header: str):
        end = link_header.find(">", self._curr)

        if end == -1:
            raise ParseError()

        href = link_header[self._curr + 1:end]
        self._curr = end + 1

        return href

    def _parse_attributes(self, link_header):
        end = link_header.find("=", self._curr)
        if end == -1:
            raise ParseError()

        name = link_header[self._curr: end].strip()
        self._curr = end + 1
        val = ""

        if not self._curr >= len(link_header):
            if link_header[self._curr] == '"':

                self._curr = self._curr + 1
                end = link_header.find('"', self._curr)

                if end == -1:
                    raise ParseError()
                val = link_header[self._curr: end]
                self._curr = end + 1

        return name, val

    @staticmethod
    def _transform(href: str, attributes: dict) -> LinkParserResult:
        relationship = attributes.get("rel", "")
        link_type = attributes.get("type", "")
        datetime = attributes.get("datetime", "")
        title = attributes.get("title", "")
        link_from = attributes.get("from", "")
        link_until = attributes.get("until", "")

        return LinkParserResult(
            uri=href, relationship=relationship, link_type=link_type, datetime=datetime, title=title,
            link_from=link_from, link_until=link_until
        )
