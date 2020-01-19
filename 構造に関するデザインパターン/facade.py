import os
import gzip
import tarfile
import zipfile


def main():
    f_name_zip = "_temp/test.zip"
    f_name_tar = "_temp/test.tar.gz"
    f_name_gz = "_temp/test.gz"

    for f_name in [f_name_zip, f_name_tar, f_name_gz]:
        with Archive(f_name) as archive:
            print(archive.names())
            archive.unpack()


class Archive:

    def __init__(self, filename):
        self._names = None
        self._unpack = None
        self._file = None
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name):
        self.close()
        self.__filename = name

    def close(self):
        if self._file is not None:
            self._file.close()

    def names(self):
        if self._file is None:
            self._prepare()
        return self._names()

    def unpack(self):
        if self._file is None:
            self._prepare()
        self._unpack()

    def _prepare(self):
        if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
            self._prepare_tarball_or_zip()
        elif self.filename.endswith(".gz"):
            self._prepare_gzip()
        else:
            raise ValueError("unreadable format: {}".format(self.filename))

    def _prepare_tarball_or_zip(self):
        def ext_all():
            self._file.extractall()

        if self.filename.endswith(".zip"):
            self._file = zipfile.ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = ext_all
        else:
            suffix = os.path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, "r:" + suffix[1:])
            self._names = self._file.getnames
            self._unpack = ext_all

    def _prepare_gzip(self):
        self._file = gzip.open(self.filename)
        filename = os.path.splitext(self.filename)[0]
        self._names = lambda: [filename]

        def extractall():
            with open(filename, "wb") as f:
                f.write(self._file.read())
        self._unpack = extractall

    def __str__(self):
        return "{}({})".format(self.filename, self._file is not None)

    # 以下2つは、コンテキストマネジャーに必要なメソッド。
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    main()
