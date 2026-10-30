import os
from pathlib import Path

import requests
from tqdm import tqdm

from .utils.platform import generated_name

__GONEONIZE_VERSION__ = "0.3.13"
__GIT_RELEASE_URL__ = "https://github.com/Nubuki-all/neonize"


class UnsupportedPlatform(Exception):
    pass


def library_path(versioned: bool = True) -> Path:
    """Where the goneonize shared library lives.

    Downloaded libraries carry their version in the file name, so upgrading
    neonize with pip never picks up a library left behind by an older version
    (pip doesn't know about files downloaded at runtime and leaves them in
    place). The unversioned name is the library bundled into wheels and local
    builds, next to a ``.version`` marker naming its version.
    """
    name = Path(generated_name())
    if not versioned:
        return Path(__file__).parent / name.name
    return Path(__file__).parent / f"{name.stem}-{__GONEONIZE_VERSION__}{name.suffix}"


def __download(url: str, fname: str, chunk_size=1024):
    resp = requests.get(url, stream=True, timeout=30)
    if resp.status_code != 200:
        resp.close()
        raise UnsupportedPlatform(generated_name())
    total = int(resp.headers.get("content-length", 0))
    with (
        open(fname, "wb") as file,
        tqdm(
            desc=Path(fname).name,
            total=total,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar,
    ):
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)
        bar.n = total
    bar.close()


def download() -> Path:
    """Download this version's library and return its path.

    The file is written under a temporary name and renamed into place, so a
    library that is already loaded is never overwritten.
    """
    dest = library_path()
    part = dest.with_name(dest.name + ".part")
    try:
        __download(
            f"{__GIT_RELEASE_URL__}/releases/download/{__GONEONIZE_VERSION__}/{generated_name()}",
            str(part),
        )
        os.replace(part, dest)
    finally:
        part.unlink(missing_ok=True)
    return dest


if __name__ == "__main__":
    download()
