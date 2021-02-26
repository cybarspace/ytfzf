#!/usr/bin/env python3
# cython: language_level=3
"""
Script to play media from YouTube
"""
# required imports
from urllib import request
from urllib import parse
import getopt
import sys
import os
import re


def get_media_url(search_str="rickroll"):
    """
    Function to get media URL
    """
    query_string = parse.urlencode({"search_query": search_str})
    html_content = (
        request.urlopen("https://www.youtube.com/results?" + query_string)
        .read()
        .decode()
    )
    search_results = re.findall(r'"videoId":"(.{11})"', html_content)
    media_url = "https://www.youtube.com/watch?v=" + search_results[0]
    return media_url


# main program logic
if __name__ == "__main__":
    # parse arguments
    try:
        opts, extras = getopt.getopt(sys.argv[1:], "hv:")

        # decide whether to play video or audio only for the session
        if len(opts) == 0 or "-h" in opts[0]:
            print("ytplay [-v] <search-query>")
            sys.exit()
        elif "-v" in opts[0]:
            FLAGS = "--ytdl-format=best"
            req_search = opts[0][1] + " ".join(extras).rstrip()
        else:
            FLAGS = "--ytdl-format=bestaudio --no-video"
            req_search = " ".join(extras).strip()

    except getopt.GetoptError:
        print("ytplay [-v] <search-query>")
        sys.exit(2)

    # play the requested item and loop over input
    while req_search != "q":
        os.system(f"mpv {FLAGS} {get_media_url(req_search)}")
        answer = input("Repeat? (y/n): ")
        if answer == "n":
            req_search = input("Play next (q to quit): ")
        elif answer == "y":
            continue
        else:
            break

    sys.exit()
