import sys


# Geohashing is an outdoor recreational activity inspired by the xkcd webcomic,
# in which participants have to reach a random location (chosen by a computer
# algorithm), prove their achievement by taking a picture of a Global
# Positioning System (GPS) receiver or another mobile device and then tell the
# story of their trip online.
# Proof based on non-electronic navigation is also acceptable.


def check_date_format(date):
    # check if the date is in the correct format
    # YYYY-MM-DD-XXXXX.XX
    # YYYY: year
    # MM: month
    # DD: day
    # XXXXX.XX: a float number

    if not isinstance(date, str):
        return False

    date = date.split("-")

    if len(date) != 4:
        return False

    year, month, day, float_num = date

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False
    if not float_num.replace(".", "").isdigit():
        return False
    if not float_num.count(".") == 1:
        return False
    split_float = float_num.split(".")
    if len(split_float[0]) != 5 or len(split_float[1]) != 2:
        return False
    if not split_float[0].isdigit() or not split_float[1].isdigit():
        return False

    return True


def check_lat_lon(lat, lon):
    # check if the latitude and longitude are in the correct format
    # latitude: -90 to 90
    # longitude: -180 to 180
    if lat >= -90 and lat <= 90 and lon >= -180 and lon <= 180:
        return True
    return False


def parse_arguments():

    if len(sys.argv) != 4:
        print(
            "Usage: python geohashing.py <latitude> <longitude> <date>\n"
            "Example:\n" +
            "python3 geohashing.py 37.421542 -122.085589 '2005-05-26-10458.68'\n"
        )
        exit()

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    date = sys.argv[3]

    if not check_lat_lon(lat, lon):
        raise ValueError("Invalid latitude or longitude")
    elif not check_date_format(date):
        raise ValueError("Invalid date format")

    return lat, lon, date.encode()


# def geohash(lat: str, lon: str, date: str):

#     """
#     My implementation of the geohash function based on :
#     https://xkcd.com/426/
#     """

#     import hashlib

#     # md5 the date
#     date_hash = hashlib.md5(date, usedforsecurity=False).hexdigest()

#     # split the date hash into two parts
#     first_16 = date_hash[:16]
#     last_16 = date_hash[-16:]

#     # convert to the str to 0.XXXXX with XXXXX being the 16 hexa characters
#     first_16 = int(first_16, 16) * 16**-16
#     last_16 = int(last_16, 16) * 16**-16

#     # split the latitude and longitude
#     split_lat = str(lat).split(".")
#     split_lon = str(lon).split(".")

#     # calculate the geohash
#     float_lat = float(split_lat[0])
#     float_lon = float(split_lon[0])

#     # add the first 16 and last 16 to the latitude and longitude first part
#     # if the latitude or longitude is negative, subtract the value
#     # if the latitude or longitude is positive, add the value
#     if float_lat > 0:
#         lat_geohash = float_lat + first_16
#     else:
#         lat_geohash = float_lat - first_16

#     if float_lon > 0:
#         lon_geohash = float_lon + last_16
#     else:
#         lon_geohash = float_lon - last_16

#     # print the latitude and longitude with a precision of 6
#     print(f"{lat_geohash:.6f} {lon_geohash:.6f}")


def main():

    lat, lon, date = parse_arguments()

    # The import is here to avoid boring
    from antigravity import geohash

    geohash(lat, lon, date)

    # geohash(lat, lon, date)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
