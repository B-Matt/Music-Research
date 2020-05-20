from azure.storage.blob import BlockBlobService
import os

class BlobStorage(object):
	account_name = "mrsongs"
	account_key = "PbaD3PTZtvWqWB1jhYpZogPQ0TrGSV39vWnJkb4ToMmH7NIwJW4/XO65H3ifN8nSrFe57NLHjeIjCmeK2IpvMQ=="
	endpoint_suffix = "core.windows.net"
	storage_container = "assets"
	storage_sas = "https://mrsongs.blob.core.windows.net/assets?sp=racwdl&st=2020-02-21T14:27:12Z&se=2022-02-22T14:27:00Z&sv=2019-02-02&sr=c&sig=ev65N9sg7V8czIwlnlTNYlf4AJ%2FEDC13PRzttFgnZQk%3D"
	
	def __init__(self):
		self.blob_service = BlockBlobService(account_name=self.account_name, account_key=self.account_key, sas_token=self.storage_sas, endpoint_suffix=self.endpoint_suffix)
	
	def format_blob_path(self, blob_name):
		"""
        Formats full URI's for given Blob on Azure's BlobStorage.

		:params blob_name: The name of the Blob from which the path is generated.

        Returns
        -------
		full_blob_uri : String
                Full Blob URI from Storage (https://mrsongs.blob.core.windows.net/assets/uuid/music.mp3)
		
		blob_uri : String
				Blob URI from Storage WITHOUT file (https://mrsongs.blob.core.windows.net/assets/uuid/)        
        """
		storage_uri = "https://mrsongs.blob.core.windows.net/assets/"
		full_blob_uri = (storage_uri + blob_name)
		blob_uri = (storage_uri + os.path.dirname(blob_name))
		return full_blob_uri, blob_uri

	def remove_blob(self, blob_name):
		"""
		Removes given blob from the storage_container.

		:params blob_name: The name of the Blob that will be removed from the storage container (eg. 9e8049f1-52ab-4222-9c44-0d000363ea7d/music.mp3 (folder/file.mp3)).

		Returns
        -------
		None
		"""
		self.blob_service.delete_blob(self.storage_container, blob_name, snapshot = None)
