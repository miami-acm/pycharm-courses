from fs import open_fs

documents_folder = open_fs('~/Downloads/')
with documents_folder:
    for filename in documents_folder.listdir('/'):  # type: str
        print(filename)

    # documents_folder is automatically closed
    # when leaving the ``with`` statement
