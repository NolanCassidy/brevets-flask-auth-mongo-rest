"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    speeds = [(200,15,34),(400,15,32),(600,15,30),(1000,11.428,28),(1300,13.333,26)]

    check = control_dist_km - (brevet_dist_km * 1.2)
    if (check >1):
        return flask.render_template('404.html'), 404

    if(control_dist_km<brevet_dist_km):
        control=control_dist_km
    else:
        control=brevet_dist_km

    i, time, distance = 0, 0, 0
    while((distance + control) > speeds[i][0]):
        time += (speeds[i][0] - distance)/speeds[i][2]
        control -= (speeds[i][0] - distance)
        distance += (speeds[i][0] - distance)
        i += 1

    time += control / speeds[i][2]
    minute = time % 1
    hour = time - minute

    a = arrow.get(brevet_start_time).shift(days=1,hours=(-4+hour),minutes=round(minute * 60))
    return a.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    speeds = [(200,15,34),(400,15,32),(600,15,30),(1000,11.428,28),(1300,13.333,26)]

    check = control_dist_km - (brevet_dist_km * 1.2)
    if (check >1):
        return flask.render_template('404.html'), 404

    if (control_dist_km >= brevet_dist_km):
        max = {200:1330, 300:2000, 400:2700, 600:4000, 1000:7500}
        a = arrow.get(brevet_start_time).shift(days=1,hours=(-4+(max[brevet_dist_km]//100)),minutes =  max[brevet_dist_km]%100)
    else:
        control = control_dist_km
        i, time, distance = 0, 0, 0
        while((distance + control) > speeds[i][0]):
                time += (speeds[i][0] - distance)/speeds[i][1]
                control -=  (speeds[i][0] - distance)
                distance += (speeds[i][0] - distance)
                i += 1

        time += control / speeds[i][1]
        minute = time % 1
        hour = time - minute

        a = arrow.get(brevet_start_time).shift(days=1,hours=(-4+hour),minutes=round(minute * 60))
    return a.isoformat()
