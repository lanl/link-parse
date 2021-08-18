import re

from linkparse.link_parser import LinkParser, LinkParserResult


class RegexLinkParser(LinkParser):
    """
    Regex based link header parses the link header using predetermined regular expressions.

    First determines splitting points and afterwards extracts parameters based on the regular expressions.

    """
    _split_point = ""

    def __init__(self, split_point="[,]\s*[<]"):
        """
        Constructor for RegexLinkParser Object.

        :param split_point: regular expression used to determine the splitting points.
        """
        self._split_point = split_point

    def parse(self, link_header: str) -> list[LinkParserResult]:
        """
        Parses given link header string into link parser results.

        :param link_header: link header as string.
        :return: List containing link parser results.
        """
        link_header = link_header.strip()

        _link_parser_result = []

        split_point = re.compile(self._split_point)

        link_header_splits = [x.replace('>', '').replace('<', '') for x in split_point.split(link_header)]
        # link_header_splits = [x.replace('>', '').replace('<', '') for x in link_header.split(', <')]

        for item in link_header_splits:
            # relationship is mandatory
            relationships = re.findall('((?<=rel=")[^"]*)', item)

            # Append only if theres relationship
            if relationships:
                link = item.split(";")[0]
                relationship = relationships[0].strip()

                link_type = (re.findall('((?<=type=")[^"]*)', item) or [""])[0]
                datetime = (re.findall('((?<=datetime=")[^"]*)', item) or [""])[0]
                title = (re.findall('((?<=title=")[^"]*)', item) or [""])[0]
                link_from = (re.findall('((?<=from=")[^"]*)', item) or [""])[0]
                link_until = (re.findall('((?<=until=")[^"]*)', item) or [""])[0]
                # License needed ??
                # lic = (re.findall('((?<=license=")[^"]*)', item) or [""])[0]

                _link_parser_result.append(
                    LinkParserResult(uri=link,
                                     relationship=relationship,
                                     link_type=link_type,
                                     datetime=datetime,
                                     title=title,
                                     link_from=link_from,
                                     link_until=link_until)
                )

        return _link_parser_result
