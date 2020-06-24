import React from "react";
import axios from "axios";

const { BlobServiceClient } = require("@azure/storage-blob");

export default class HttpClient extends React.Component {
  constructor() {
    super();
    this.blobUrl = "https://mrsongs.blob.core.windows.net/";
    this.vmUrl = "http://musicresearch.northeurope.cloudapp.azure.com:8888/";
  }

  upload = async (file, uuid) => {
    const STORAGE_ACCOUNT_NAME = "mrsongs";
    const CONTAINER_NAME = "assets/" + uuid;
    // for browser, find SAS_TOKEN from API?
    const SAS_TOKEN = process.env.REACT_APP_SAS_KEY;
    const sasURL = `https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/${SAS_TOKEN}`;

    const blobServiceClient = new BlobServiceClient(sasURL);
    const containerClient = blobServiceClient.getContainerClient(
      CONTAINER_NAME
    );

    const ext = file.name.substring(file.name.lastIndexOf("."));
    const blobName = "music" + ext;
    const blockBlobClient = containerClient.getBlockBlobClient(blobName);
    return await blockBlobClient.uploadBrowserData(file);
  };

  getSongs = async () => {
    var response = await axios.get("db/songs", {
      headers: { "Access-Control-Allow-Origin": "*" },
    });
    return response.data;
  };

  getGenre = async (genreName) => {
    var response = await axios.get("db/genre", {
      params: { name: genreName },
      headers: { "Access-Control-Allow-Origin": "*" },
    });
    return response.data;
  };

  findGenre = async (id) => {
    var response = await axios.get("tcp/" + id, {
      headers: { "Access-Control-Allow-Origin": "*" },
    });
    return response.data;
  };

  put = async (item) => {
    var response = await axios.put("db/" + item.Id, item, {
      headers: { "Access-Control-Allow-Origin": "*" },
    });
    return response.data;
  };

  remove = async (id) => {
    var response = await axios.delete("db/" + id, {
      headers: { "Access-Control-Allow-Origin": "*" },
    });
    return response.data;
  };

  postSong = async (song) => {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify(song),
    };

    const response = await fetch("db", requestOptions);
    return response;
  };
}
