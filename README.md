# Eve

Eve is the **eve**nt catalogue service.
It queries an FDSN webservice and outputs an quakeml file.

Why `eve`? Because it can be on the first place of our RIESGOS
scenario pipeline - but it is the second implementation after
the quakeledger process.

## Copyright & License
Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Authors

- [Nils Brinckmann](https://www.gfz-potsdam.de/staff/nils-brinckmann/)


## Contributing

This service was created in context of the [RIESGOS procject](http://riesgos.de).
You can ask the following persons to become involved:

- Elisabeth Schöpfer (DLR)
- Fabrice Cutton (GFZ - Section 2.6)
- Juan Camilo Gomez-Zapata (GFZ - Section 2.6)
- Matthias Rüster (GFZ - Section 5.2)
- Nils Brinckmann (GFZ - Section 5.2)


## Requirements

This is a python3 program using the following libraries:

- requests
- typer


## Setup

To setup the service you can run:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

Once the setup is done you can run eve - and query come events for Chile:

```bash
./eve.py -- -73.06 -69.37 -31 -29 2022-01-01 2022-02-01 0 10 0 150
```

Please note: We use `--` in order to make python clear that the negative numbers are no flags for other arguments.

It will search in Chile for Janurary 2022 up to magnitude of 10 and a depth
of 150 km.

The comment will create a file `output.xml` with the following content:

```xml
<eventParameters xmlns="http://quakeml.org/xmlns/bed/1.2" publicID="smi:org.gfz-potsdam.de/geofon/EventParameters">
  <event publicID="smi:org.gfz-potsdam.de/geofon/gfz2022bdpy">
    <description>
      <text>Off Coast of Central Chile</text>
      <type>region name</type>
    </description>
    <creationInfo>
      <agencyID>GFZ</agencyID>
      <creationTime>2022-01-17T05:01:31.470592Z</creationTime>
    </creationInfo>
    <magnitude publicID="smi:org.gfz-potsdam.de/geofon/Origin/20220117051054.106.2572256/netMag/M">
      <stationCount>11</stationCount>
      <creationInfo>
        <agencyID>GFZ</agencyID>
        <creationTime>2022-01-17T05:10:54.194519Z</creationTime>
      </creationInfo>
      <mag>
        <value>4.59</value>
      </mag>
      <type>M</type>
      <originID>smi:org.gfz-potsdam.de/geofon/Origin/20220117051054.106.2572256</originID>
      <methodID>smi:org.gfz-potsdam.de/geofon/weighted_average</methodID>
    </magnitude>
    <origin publicID="smi:org.gfz-potsdam.de/geofon/Origin/20220117051054.106.2572256">
      <time>
        <value>2022-01-17T04:59:32.76Z</value>
        <uncertainty>0.34</uncertainty>
      </time>
      <longitude>
        <value>-72.031</value>
        <uncertainty>5.23</uncertainty>
      </longitude>
      <latitude>
        <value>-29.968</value>
        <uncertainty>1.95</uncertainty>
      </latitude>
      <quality>
        <associatedPhaseCount>41</associatedPhaseCount>
        <usedPhaseCount>30</usedPhaseCount>
        <associatedStationCount>41</associatedStationCount>
        <usedStationCount>30</usedStationCount>
        <standardError>1.33</standardError>
        <azimuthalGap>192</azimuthalGap>
        <maximumDistance>60.09</maximumDistance>
        <minimumDistance>1.09</minimumDistance>
        <medianDistance>4.51</medianDistance>
      </quality>
      <evaluationMode>automatic</evaluationMode>
      <creationInfo>
        <agencyID>GFZ</agencyID>
        <creationTime>2022-01-17T05:10:54.106302Z</creationTime>
      </creationInfo>
      <depth>
        <value>10000</value>
      </depth>
      <methodID>smi:org.gfz-potsdam.de/geofon/LOCSAT</methodID>
      <earthModelID>smi:org.gfz-potsdam.de/geofon/iasp91</earthModelID>
    </origin>
    <preferredOriginID>smi:org.gfz-potsdam.de/geofon/Origin/20220117051054.106.2572256</preferredOriginID>
    <preferredMagnitudeID>smi:org.gfz-potsdam.de/geofon/Origin/20220117051054.106.2572256/netMag/M
    </preferredMagnitudeID>
  </event>
</eventParameters>
```

Depending on the query you may get no results or a large list of `<event>` 
entries.


For the range of parameters that you can use run

```bash
./eve.py --help
```

## Documentation

Eve uses the FDSN service described here:
https://www.fdsn.org/webservices/fdsnws-event-1.2.pdf

## Feedback

If you have any feedback, please reach out to us at nils.brinckmann@gfz-potsdam.de or matthias.ruester@gfz-potsdam.de


## Running Tests

Currently there are no tests.

There are only the `run_with_result.sh` and `run_without_result.sh` 
scripts that can produce outputs that can be used to check if it
creates valid quakeml.

You can use the `QuakeML-BED-1.2.xsd` from the quakeledger repo and
run:

```bash
xmllint --schema /path/to/quakeledger/QuakeML-BED-1.2.xsd output.xml --noout
```

