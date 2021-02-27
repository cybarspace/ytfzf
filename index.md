# ytplay

### A Python3 script that helps you find YouTube videos without needing API keys, and opens or downloads it using mpv and youtube-dl.

PS: It works just like music bots on Discord - plays or downloads the first search result.

### Usage
```
Usage: ytplay [OPTIONS] <search query>
           OPTIONS:
             -h                    Show help text
             -d  <search query>    Download video
             -v  <search query>    Play video
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
- Download the file from the Releases page: [link](https://github.com/cybarspace/ytplay/releases/download/v1.0.0/ytplay.py)
- Place it in your $PATH and make it executable.
- Enjoy!
