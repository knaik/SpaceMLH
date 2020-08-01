import datetime as dt
from pytz import timezone
from skyfield import almanac
from skyfield.api import Topos, load
from flask import Flask

app = Flask(__name__)

# Figure out local midnight.
zone = timezone('US/Eastern')
now = zone.localize(dt.datetime.now())
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
next_midnight = midnight + dt.timedelta(days=1)

ts = load.timescale(builtin=True)
t0 = ts.from_datetime(midnight)
t1 = ts.from_datetime(next_midnight)
eph = load('de421.bsp')
bluffton = Topos('40.8939 N', '83.8917 W')
f = almanac.dark_twilight_day(eph, bluffton)
times, events = almanac.find_discrete(t0, t1, f)

timings =  []


for t, e in zip(times, events):
    tstr = str(t.astimezone(zone))[:16]
    timings.append(str(tstr + ' ' +  almanac.TWILIGHTS[e]+ 'starts'))


@app.route('/')
def hello():
    return ', '.join(map(str, timings))


if __name__ == '__main__':
    app.run()
