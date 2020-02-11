import React from 'react';
import axios from 'axios';

export default class HttpClient extends React.Component {

    constructor() {
        super();
        this.webApiUrl = "https://localhost:3000/";
    }

    uploadSong = async (blob) => {
        return axios({
            method: 'post',
            url: '',
            timeout: 3000,
            data: {
                blob: blob,
            }
        }).then(response => {
            return {
                status: response.status,
                data: response.data
            }
        })
    }


}