from dataclasses import dataclass


@dataclass
class MainSearchForm:
    first_date_delta: int
    second_date_delta: int
    regions: list
    trip_types: list
    difficult: list