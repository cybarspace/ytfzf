# ytplay

### A Python3 script that helps you find YouTube videos without needing API keys, and opens it using mpv/youtube-dl.
<!--/downloads-->

PS: It works like music bots on Discord - plays the first search result.

# Usage
```
Usage: ytplay [OPTIONS] <search query>
	OPTIONS:
    -h                    Show this help text
    -v  <search query>    Play video (audio-only if not specified)
```
<!---d  <search query>    Download to current directory-->

## Examples
> Stream audio (music)

	ytplay <search-query>

> Watch video

	ytplay -v <search-query>

<!--> Download a video (planned feature)

	ytplay -d <search-query>-->

# Dependencies
- [Python 3](https://www.python.org/downloads/) (tested on PyPy 3.7.9 and CPython 3.9.1)
- [mpv](https://github.com/mpv-player/mpv)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)

# Installation

	git clone https://github.com/cybarspace/ytplay
	cd ytplay
	chmod +x ytplay.py

Copy it to your path

	sudo cp ytplay.py /usr/local/bin/ytplay
