from pathlib import Path
import os
import re
import youtube_dl
import datetime
import fire

OUTPUT_DIR = Path("downloaded_videos")
CONTENT_DIR = Path("content")


def generate_youtube_links(path):
    """ go through all the markdown files in content and yield all the youtube urls.
    """
    if path.is_dir():
        for child in os.listdir(path):
            for link in generate_youtube_links(path / child):
                yield link
    elif path.suffix == ".md":
        with open(path, "r") as f:
            for line in f:
                # found = re.search("\((https://youtu.*)\)", line)
                found = re.search("(https://w{0,3}\.?youtu.*)\)", line)
                if found:
                    for link in found.groups():
                        yield path, link


def _download_entries(ydl, entries, start_time, delta):

    directory_contents = os.listdir(".")
    downloaded_titles = [
        ".".join(s.split(".")[:-1]) for s in directory_contents
    ]  # remote ever

    for entry in entries:
        title = entry["title"]
        video_id = entry["id"]
        filename = f"{title}-{video_id}"
        if filename not in downloaded_titles:
            # we haven't downloaded it yet
            print(f"downloading {title}")
            url = entry["webpage_url"]
            try:
                ydl.download([url])
            except youtube_dl.utils.DownloadError as e:
                print(f"Error: {e}")
            # yes, we are explicitly silencing the error
            # the video might have been deleted

        if datetime.datetime.now() - start_time >= delta:
            print("--- we're out of time! ---")
            exit()


def download_all(cutoff_after_n_hours=1):
    start_time = datetime.datetime.now()
    delta = datetime.timedelta(hours=cutoff_after_n_hours)

    print("============================")
    print("starting downloads...")
    print(f"CUTOFF TIME = {start_time+delta}")
    print("============================")

    cwd = os.getcwd()
    for path, link in generate_youtube_links(CONTENT_DIR):
        print()
        print(f"downloading {path} : {link}")
        final_dir = OUTPUT_DIR / path.relative_to(CONTENT_DIR).parent
        os.makedirs(final_dir, exist_ok=True)

        os.chdir(final_dir)

        with youtube_dl.YoutubeDL({}) as ydl:
            info = ydl.extract_info(
                link,
                force_generic_extractor=ydl.params.get(
                    "force_generic_extractor", False
                ),
                download=False,
            )

            if "entries" in info:
                print("looks like this is a playlist...")
                _download_entries(
                    ydl, info["entries"], start_time, delta
                )  # it's a playlist
            else:
                print("single entry")
                _download_entries(ydl, [info], start_time, delta)  # just one video

        os.chdir(cwd)


if __name__ == "__main__":
    fire.Fire(download_all)
