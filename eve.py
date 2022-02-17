#!/usr/bin/env python3

"""
Eve

The **eve**nt catalogue service.

A python script to query events from an fdsn service.
"""

from datetime import datetime
from enum import Enum

import typer

from fdsn import Fdsn
from quakeml import to_valid_quakeml


class Provider(str, Enum):
    """Possible provider values for the fdsn service."""

    GFZ = "gfz"


KNOWN_FDSN_SERVICE_PROVIDER = {
    Provider.GFZ: "https://geofon.gfz-potsdam.de/fdsnws/"
}


def main(
    # First the bounding box
    lonmin: float = typer.Argument(
        None,
        help="".join(
            [
                "The minimum longitude of the search bounding ",
                "box in decimal degree.",
            ]
        ),
    ),
    lonmax: float = typer.Argument(
        None,
        help="".join(
            [
                "The maximum longitude of the search ",
                "bounding box in decimal degree.",
            ]
        ),
    ),
    latmin: float = typer.Argument(
        None,
        help="".join(
            [
                "The minimum latitude of the search bounding ",
                "box in decimal degree.",
            ]
        ),
    ),
    latmax: float = typer.Argument(
        None,
        help="".join(
            [
                "The maximum latitude of the search bounding ",
                "box in decimal degree.",
            ]
        ),
    ),
    # Then the time restristions
    starttime: datetime = typer.Argument(
        None, help="The start of the time interval to search for (UTC)."
    ),
    endtime: datetime = typer.Argument(
        None, help="The end of the time interval to search for (UTC)."
    ),
    # And then magnitude
    mmin: float = typer.Argument(
        None, help="The minimum magnitude to search for."
    ),
    mmax: float = typer.Argument(
        None, help="The maximum magnitude to search for."
    ),
    # and depth
    zmin: float = typer.Argument(None, help="Minimal depth in km."),
    zmax: float = typer.Argument(None, help="Maximal depth in km."),
    # The last one is the limit, so that we don't
    # query all of the catalogue.
    limit: int = typer.Argument(200, help="The limit of events to query."),
    provider: Provider = typer.Argument(
        Provider.GFZ, help="The fdsn provider to query."
    ),
):
    """Eve - the **eve**nt catalogue."""
    fdsn_service = Fdsn(KNOWN_FDSN_SERVICE_PROVIDER[provider])
    events = fdsn_service.query_events(
        minlatitude=latmin,
        maxlatitude=latmax,
        minlongitude=lonmin,
        maxlongitude=lonmax,
        starttime=starttime,
        endtime=endtime,
        mindepth=zmin,
        maxdepth=zmax,
        minmagnitude=mmin,
        maxmagnitude=mmax,
        limit=limit,
    )
    events_valid_quakeml = to_valid_quakeml(events)

    output_file = "output.xml"
    with open(output_file, "w") as outfile:
        outfile.write(events_valid_quakeml)


if __name__ == "__main__":
    typer.run(main)
