from fs import open_fs

downloads_folder = open_fs('~/Downloads/')
with downloads_folder:
    for filename in downloads_folder.listdir('/'):  # type: str
        print(filename)

    # documents_folder is automatically closed
    # when leaving the ``with`` statement
