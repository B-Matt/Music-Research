"""
    (c) 2020. Matej Arlović, Franjo Josip Jukić
"""
import os, uuid
from azure.storage.blob import BlockBlobService

class BlobStorage(object):
    """
    """
    def __init__(self):
        self.storage_account_name = os.environ.get("STORAGE_ACCOUNT_NAME")
        self.storage_account_key = os.environ.get("STORAGE_ACCOUNT_KEY")
        self.storage_endpoint_suffix = os.environ.get("STORAGE_ACCOUNT_ENDPOINT_SUFFIX")
        self.storage_container = os.environ.get("STORAGE_CONTAINER")
        self.block_blob_service = BlockBlobService(account_name=self.storage_account_name, account_key=self.storage_account_key, endpoint_suffix=self.storage_endpoint_suffix)

    def list_container_blobs(self):
        generator = self.block_blob_service.list_blobs(self.storage_container)
        response = ""
        for blob in generator:
            response += (blob.name + "\n")        
        return response

    def get_blob_folder(self, uuid):
        generator = self.block_blob_service.list_blobs(self.storage_container, prefix=(uuid + "/"))
        return len(list(generator)) == 1