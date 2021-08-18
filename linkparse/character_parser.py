from linkparse.link_parser import LinkParserResult, LinkParser


class CharacterLinkParser(LinkParser):
    """

    State Machine based link parser parses the link header character by character (character based state transitions).
    Used in the initial implementation of memento validator.

    Original dictionary based result transformed into linkparser library return formats.

    Author: Luda Balakirawa (ludab@lanl.gov)

    """

    def parse(self, link_header: str) -> list[LinkParserResult]:
        """
        Parses given link header string into link parser results.

        :param link_header: link header as string.
        :return: List containing link parser results.
        """
        state = "start"
        link_header = link_header.strip()
        data = [d for d in link_header]
        links = {}

        while data:
            if state == "start":
                d = data.pop(0)
                while d.isspace():
                    d = data.pop(0)
                if d != "<":
                    # raise ValueError("Expected < in start, got %s" % d)
                    return self._transform({})
                state = "uri"
            elif state == "uri":
                uri = []
                d = data.pop(0)
                while d != ">":
                    uri.append(d)
                    d = data.pop(0)
                uritmp = [">"]
                if not data:
                    return self._transform({})
                d = data.pop(0)
                while d.isspace():
                    uritmp.append(d)
                    d = data.pop(0)
                if d in [",", ";"]:
                    uri = "".join(uri)
                    # uri = uri[:-1]
                    # Not an error to have the same URI multiple times (I think!)
                    if not uri in links.keys():
                        links[uri] = {}
                    state = "paramstart"
                else:
                    uritmp.append(d)
                    uri.extend(uritmp)

            elif state == "paramstart":
                # d = data.pop(0)
                while data and d.isspace():
                    d = data.pop(0)
                if d == ";":
                    state = "linkparam"
                elif d == ",":
                    state = "start"
                else:
                    return self._transform({})
                    # raise ValueError("Expected ; in paramstart, got %s" % d)
            elif state == "linkparam":
                d = data.pop(0)
                while d.isspace():
                    d = data.pop(0)
                paramType = []
                while not d.isspace() and d != "=":
                    paramType.append(d)
                    d = data.pop(0)
                while d.isspace():
                    d = data.pop(0)
                if d != "=":
                    return {}
                    # raise ValueError("Expected = in linkparam, got %s" % d)
                state = "linkvalue"
                pt = "".join(paramType)
                if not pt in links[uri].keys():
                    links[uri][pt] = []
            elif state == "linkvalue":
                d = data.pop(0)
                while d.isspace():
                    d = data.pop(0)
                paramValue = []
                if d == """:
                    pd = d
                    d = data.pop(0)
                    while d != """ and pd != "\\":
                        paramValue.append(d)
                        pd = d
                        d = data.pop(0)
                else:
                    while not d.isspace() and not d in (",", ";"):
                        paramValue.append(d)
                        if data:
                            d = data.pop(0)
                        else:
                            break
                    if data:
                        data.insert(0, d)
                state = "paramstart"
                if data:
                    d = data.pop(0)
                pv = "".join(paramValue)
                if pt == "rel":
                    # rel types are case insensitive and space separated
                    links[uri][pt].extend([y.lower() for y in pv.split(" ")])
                else:
                    if not pv in links[uri][pt]:
                        links[uri][pt].append(pv)

        return self._transform(links)

    def _transform(self, links: dict) -> [LinkParserResult]:
        _link_parser_results = []

        for key in links.keys():
            value: dict = links[key]
            relationships = value.get("rel", [""])
            for relationship in relationships:
                _link_parser_results.append(
                    LinkParserResult(uri=key,
                                     relationship=relationship,
                                     link_type=value.get("type", [""])[0],
                                     datetime=value.get("datetime", [""])[0],
                                     title=value.get("title", [""])[0],
                                     link_from=value.get("from", [""])[0],
                                     link_until=value.get("until", "")[0])
                )

        return _link_parser_results