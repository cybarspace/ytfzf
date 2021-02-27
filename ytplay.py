#!/usr/bin/env python3
# cython: language_level=3
"""
Script to play media from YouTube

@author: Sheikh Saad Abdullah
My Github: https://github.com/cybarspace
"""
# required imports
from shutil import (
    which as installed,
)  # to check if required dependencies are installed
from urllib import request  # to get data from YouTube
from urllib import parse  # to parse data obtained
import getopt  # to parse command-line arguments
import sys  # to exit with error codes
import os  # to execute media player
import re  # to find media URL from search results


def error(err_code=0, msg="", **kwargs):
    """
    Show an error message and exit with requested error code

    @param err_code: the error code
    @param msg: the error message
    @param **kwargs: extra messages
    """
    # if no error message given...
    if len(msg) == 0:
        # set the error message to usage info
        msg = str(
            "Usage: ytplay [OPTIONS] <search query>\n"
            + "         OPTIONS:\n"
            + "         -h                    Show this help text\n"
            + "         -v  <search query>    Play video (audio-only if not specified)"
        )
    # print the given or default error message
    print(msg)
    # if any extra messages are given...
    for err, err_msg in kwargs.items():
        # print the extra messages
        print(f"{err}: {err_msg}")
    # exit with given or default error code
    sys.exit(err_code)


def check_deps(deps_list):
    """
    Check if required dependencies are installed

    @param deps_list: list of dependencies to check
    """
    # check each item in given dependency list
    # and see if it is installed on the system
    for deps in deps_list:
        # if it is not installed
        if not installed(deps):
            # show an error message and exit with code 1
            error(1, msg=f"Dependency {deps} not found.\nPlease install it.")


def get_media_url(search_str="rickroll", result=0):
    """
    Function to get media URL

    @param search_str: the string to search for
    @param result: the nth result to get
    """
    # format the given search string for use in URLs
    query_string = parse.urlencode({"search_query": search_str})
    # get the YouTube search-result page for given search string
    html_content = (
        request.urlopen("https://www.youtube.com/results?" + query_string)
        .read()
        .decode()
    )
    # find the list of video IDs from result page
    search_results = re.findall(r'"videoId":"(.{11})"', html_content)
    # if no results are found...
    if len(search_results) == 0:
        # print error message and exit
        error(msg="No results found.")
    # select the first (or given) result and deduce its URL
    media_url = "https://www.youtube.com/watch?v=" + search_results[result]
    # return the URL of requested media
    return media_url


def play(options, search_str, player="mpv"):
    """
    Call the media player and play requested media

    @param options: the command line arguments to the player
    @param search_str: the string to search for
    @param player: the media player to play audio or video with
    """
    # check if dependencies are satisfied
    check_deps((f"{player}", "youtube-dl"))
    # if everything is ok, play requested media
    os.system(f"{player} {options} {get_media_url(search_str)}")


def main():
    """
    Main program logic
    """
    # parse flags and arguments
    try:
        opts, extras = getopt.getopt(sys.argv[1:], "hv:")

        # decide whether to play video or audio only for the session
        try:
            if "-h" in opts[0]:
                error()  # show help and exit normally
            elif "-v" in opts[0]:
                # prepare to play video with default quality
                req_search = opts[0][1] + " ".join(extras).rstrip()
                flags = ""
        # when no flags are given...
        except IndexError:
            # and no arguments are given...
            if len(extras) == 0:
                # show help and exit with error code 2
                error(2, NoArgs="Nothing given to search.")
            # but if arguments are given,
            # prepare to play audio with best quality
            flags = "--ytdl-format=bestaudio --no-video"
            req_search = " ".join(extras).strip()
    # if invalid flags are used...
    except getopt.GetoptError:
        error(2, UnknownArgs="Unknown options given.")

    # play the requested item and loop over input
    while req_search != "q":
        # call the mpv media player with processed flags and URL
        play(flags, req_search)
        # when done, ask if user wants to repeat the last played media
        answer = input("Repeat? (y/n): ")
        # process user request
        if answer.lower() == "n":
            # if user answers no,
            # ask what to play next, or quit
            req_search = input("Play next (q to quit): ")
        elif answer.lower() == "y":
            # if user answers yes,
            # keep playing
            continue
        else:
            # if invalid option is chosen
            # exit with code 2
            sys.exit(2)
    # exit normally when everything is done
    sys.exit()


# when invoked as a program...
if __name__ == "__main__":
    # execute the main function and process flags and arguments accordingly
    main()
