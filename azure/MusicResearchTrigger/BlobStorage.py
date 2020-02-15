import os, uuid
from azure.storage.blob import BlockBlobService


block_blob_service = BlockBlobService(account_name="mrsongs", account_key="", endpoint_suffix="")
generator = block_blob_service.list_blobs('')

for blob in generator:
    print(blob.name)