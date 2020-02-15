import React from 'react';
import axios from 'axios';
const { BlobServiceClient } = require('@azure/storage-blob');
require('dotenv').config()

export default class HttpClient extends React.Component {

    constructor() {
        super();
        this.blobUrl = 'https://mrsongs.blob.core.windows.net/';
    }

    uploadSong = async (blob, uuid) => {
        return axios({
            mode: 'no-cors',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            method: 'post',
            url: this.blobUrl + uuid,
            timeout: 3000,
            data: blob
        }).then(response => {
            return {
                status: response.status,
                data: response.data
            }
        })
    }

    uploadBlobContainer = async (file,uuid) => {
        const STORAGE_ACCOUNT_NAME = 'mrsongs';
        const CONTAINER_NAME = 'assets/'+ uuid;
        // for browser, SAS_TOKEN is get from API?
        //missing const SAS_TOKEN = "here goes your sas token"
        const SAS_TOKEN = "";
        const sasURL = `https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/${SAS_TOKEN}`;
      
        const blobServiceClient = new BlobServiceClient(sasURL)
        const containerClient = blobServiceClient.getContainerClient(CONTAINER_NAME)
      
        const filename = "music";
        const ext = file.name.substring(file.name.lastIndexOf('.'));
        const blobName = filename + ext;
        const blockBlobClient = containerClient.getBlockBlobClient(blobName);
        return await blockBlobClient.uploadBrowserData(file);

    }




}