import re
from linkparse.link_parser import LinkParser, LinkParserResult


class MemgatorLinkParser(LinkParser):
    """
    Python version of the Regex based parser used in the Memegator implementation. Original implementation in Golang.

    Uses character traversal to find splitting points in the link header and uses regular expressions to extract
    attributes in the link header. Modified to extract all link header relations (original filters mementos)

    Author : Sawood Alam (@ibnesayeed)

    source : https://github.com/oduwsdl/MemGator

    """
    _uri_split_regex = '\s*>?"?\s*;\s*'

    _kv_extraction_regex = '\s*=\s*"?\s*'

    _special_chars = "<\" \t\n\r"

    def parse(self, link_header: str) -> list[LinkParserResult]:

        results = list()

        link_splits = self._split_links(link_header)
        for link_split in link_splits:
            for special_char in self._special_chars:
                link_split = link_split.replace(special_char, "")

            uri_split = re.split(self._uri_split_regex, link_split)[0]
            attribute_splits = re.split(self._uri_split_regex, link_split)[1:]
            attribute_map = dict()
            for attribute_split in attribute_splits:
                kv = re.split(self._kv_extraction_regex, attribute_split)
                attribute_map[kv[0]] = kv[1]

            if not 'rel' in attribute_map.keys():
                continue

            results.append(LinkParserResult(uri=uri_split,
                                            relationship=attribute_map['rel'],
                                            link_type=attribute_map.get('type', ''),
                                            datetime=attribute_map.get('datetime', ''),
                                            title=attribute_map.get('title', ''),
                                            link_from=attribute_map.get('from', ''),
                                            link_until=attribute_map.get('until', '')))

        return results

    def _split_links(self, string) -> list[str]:
        link_splits = list()
        q = False
        u = False
        i = 0
        j = 0
        while j < len(string):
            if string[j] == '"':
                q = not q
            elif string[j] == '<':
                u = True
            elif string[j] == '>':
                u = False
            elif string[j] == ',':
                if not q and not u:
                    link_splits.append(string[i:j])
                    i = j + 1
            j = j + 1

        if i < j:
            link_splits.append(string[i:j])

        return link_splits
