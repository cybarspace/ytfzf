# ytplay

### A Python3 script that helps you find YouTube videos without needing API keys, and opens or downloads it using mpv/youtube-dl.

PS: It works like music bots on Discord - plays the first search result.

### Usage
```
Usage: ytplay [OPTIONS] <search query>
           OPTIONS:
               -h                    Show this help text
               -d  <search query>    Download video
               -v  <search query>    Play video (audio-only if not specified)
```

#### Examples
- Stream audio

	`ytplay <search-query>`

- Watch a video

	`ytplay -v <search-query>`

- Download a video

	`ytplay -d <search-query>`

### Dependencies
- [Python 3](https://www.python.org/downloads/) (tested on PyPy 3.7.9 and CPython 3.9.1)
- [mpv](https://github.com/mpv-player/mpv)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [ffmpeg](https://github.com/FFmpeg/FFmpeg)

### Installation

	git clone https://github.com/cybarspace/ytplay
	cd ytplay
	chmod +x ytplay.py

Copy it to your path

	sudo cp ytplay.py /usr/local/bin/ytplay
