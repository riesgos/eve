"""
fdsn

The module to interacte with an FDSN web service.

See: https://www.fdsn.org/webservices/fdsnws-event-1.2.pdf
"""

from typing import Optional
from datetime import datetime

import requests


class Fdsn:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def query_events(
        self,
        minlatitude: Optional[float] = None,
        maxlatitude: Optional[float] = None,
        minlongitude: Optional[float] = None,
        maxlongitude: Optional[float] = None,
        starttime: Optional[datetime] = None,
        endtime: Optional[datetime] = None,
        mindepth: Optional[float] = None,
        maxdepth: Optional[float] = None,
        minmagnitude: Optional[float] = None,
        maxmagnitude: Optional[float] = None,
        limit: Optional[int] = None,
    ):
        event_query_url = self.base_url + "/event/1/query"

        parameters = {
            "format": "xml",
        }

        if minlatitude is not None:
            parameters["minlatitude"] = minlatitude
        if maxlatitude is not None:
            parameters["maxlatitude"] = maxlatitude
        if minlongitude is not None:
            parameters["minlongitude"] = minlongitude
        if maxlongitude is not None:
            parameters["maxlongitude"] = maxlongitude

        if starttime is not None:
            parameters["starttime"] = starttime
        if endtime is not None:
            parameters["endtime"] = endtime

        if mindepth is not None:
            parameters["mindepth"] = mindepth
        if maxdepth is not None:
            parameters["maxdepth"] = maxdepth
        if minmagnitude is not None:
            parameters["minmagnitude"] = minmagnitude
        if maxmagnitude is not None:
            parameters["maxmagnitude"] = maxmagnitude

        if limit is not None:
            parameters["limit"] = limit

        resp = requests.get(event_query_url, parameters)
        resp.raise_for_status()
        return resp.text
