import os
import pandas as pd

from django.core.management.base import BaseCommand
from django.conf import settings
from arcgis.models import Station


class Command(BaseCommand):

    def handle(self, *args, **options):
        df = pd.read_csv(
            os.path.join(settings.BASE_DIR, 'data/st.csv'),

            error_bad_lines=False,
        )

        count = 0
        for index, row in df.iterrows():
            st = Station(
                name=row['STATION-NAME'],
                IAGA=row['IAGA'],
                lat=row['GEOLAT'],
                lon=row['GEOLON'],
                mlon=row['AACGMLON'],
                mlat=row['AACGMLAT'],
            )
            try:
                st.save()
                count += 1
            except:
                pass

            print(f'Saved {count} / {len(df.index)} staions')
