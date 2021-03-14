from marshmallow import Schema, fields


class StationSchema(Schema):
    name = fields.String()
    IAGA = fields.String()
    lat = fields.Decimal()
    lon = fields.Decimal()
    mlat = fields.Decimal()
    mlon = fields.Decimal()
