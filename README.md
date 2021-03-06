# ytplay

![figlet](https://user-images.githubusercontent.com/50134239/109390169-2c1b9000-793a-11eb-94d4-d6b3edc631b7.png)

### A Python script that helps you find YouTube videos without needing API keys, and opens or downloads it using mpv/youtube-dl.

PS: It works just like music bots on Discord - plays or downloads the first search result.

### Installation
- Download the file from the Releases page: [link](https://github.com/cybarspace/ytplay/releases/download/v1.0.0/ytplay.py)
- Place it in your `$PATH` and make it executable.
- Enjoy!

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

### Credits
- [pystardust](https://github.com/pystardust)'s [ytfzf](https://github.com/pystardust/ytfzf)
- [This article](https://www.codeproject.com/articles/873060/python-search-youtube-for-video) I found during my quest to implement a simplified version of ytfzf in Python3

### About the `.pyx` file...

Cython is supposed to be faster but I don't really know Cython so I couldn't optimize it as well. If you can, feel free to make a fork, and maybe even a pull request so I can review and merge. It'll be a learning experience for me.

As for the performance... It may be slightly faster but the program is still network-bound. Faster internet = faster query.

Compile an executable file using [this shell script](https://github.com/cybarspace/cymake) if you want. Please note that it behaves a bit differently from the Python version. That is intentional - I wanted two "flavors".
