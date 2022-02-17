"""QuakeML related code."""

from xml.etree import ElementTree


def to_valid_quakeml(events):
    """
    Transform the quakeml text from geofon to valid quakeml.

    The geofon quakeml contains a header that we don't have in
    the quakeml xsd file. We need to deliver valid data for this
    schema alone (and not wrapped with an element from another
    schema), so that the downstream riesgos processes can work
    with the quakeml content.
    """
    if not events:
        return """<eventParameters
            xmlns="http://quakeml.org/xmlns/bed/1.2"
            publicID="smi:org.gfz-potsdam.de/geofon/EventParameters">
        </eventParameters>"""

    # The quakeml that we got from the fdsn service is not valid
    # as ti contains a root element that we don't want to have "q:quakeml")
    raw_quakeml = ElementTree.fromstring(events)
    event_parameters = raw_quakeml.find(
        "{http://quakeml.org/xmlns/bed/1.2}eventParameters"
    )
    ElementTree.register_namespace("", "http://quakeml.org/xmlns/bed/1.2")
    return ElementTree.tostring(event_parameters).decode("UTF-8")
