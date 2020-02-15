import React from 'react';
import Header from '../components/Header'
import Footer from '../components/Footer'
import HttpClient from '../common/HttpClient'
import { Button } from 'react-bootstrap';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import '../styles/home.css'

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.httpClient = new HttpClient();
        this.state = {
            step: 1,
            selectedFile: null,
            loaded: 0,
            genre: "null",
            songName: "null"
        };
        this.nextStep = this.nextStep.bind(this);
        this.onChangeHandler = this.onChangeHandler.bind(this);
        this.uploadSong = this.uploadSong.bind(this);
        this.uuidv1 = this.uuidv1.bind(this);
    }

    nextStep() {
        if (this.state.step < 3) {
            if (this.state.step === 2) {
                this.uploadSong();
            }
            this.setState({
                step: this.state.step + 1
            });
        }
        else {
            this.setState({
                step: 1,
                selectedFile: null
            });
        }
    }
    uuidv1() {
        const createUuid = require('uuid/v1');
        return createUuid();
      }
    

    async uploadSong() {
        try {
            this.httpClient.uploadBlobContainer(this.state.selectedFile, this.uuidv1()).then(response => {
                response ?
                toast.success('Upload song on Server successful!', { duration: 2000 })
                :
                toast.error('Upload song on Server failed!', { duration: 2000 })
            })
        } catch (error) {
            console.log(error);
        }
    }

    onChangeHandler = event => {
        var file = event.target.files[0];
        if (this.checkMimeType(event) && this.checkFileSize(event)) {
            this.setState({
                selectedFile: file,
                fileName: file.name
            });
        }
    }

    checkMimeType = (event) => {
        let files = event.target.files;
        let err = '';
        const types = ['audio/mp3', 'audio/wav']
        for (var x = 0; x < files.length; x++) {
            if (types.every(type => files[x].type !== type)) {
                err += files[x].type + ' is not a supported format\n';
            }
        };

        if (err !== '') {
            event.target.value = null;

            toast.error('Wrong file format, please try with .MP3 or .WAV',
                {
                    hideProgressBar: true,
                    position: "bottom-right",
                    closeOnClick: true,
                    autoClose: 4000
                });
            return false;
        }
        return true;
    }

    checkFileSize = (event) => {
        let files = event.target.files;
        let size = 30000000;
        let err = "";
        for (var x = 0; x < files.length; x++) {
            if (files[x].size > size) {
                err += files[x].type + ' is too large, please pick a smaller file\n';
            }
        };
        if (err !== '') {
            event.target.value = null;
            toast.error('File is too large, please pick a smaller file (MAX 30MB)',
                {
                    hideProgressBar: true,
                    position: "bottom-right",
                    closeOnClick: true,
                    autoClose: 4000
                });
            return false;
        }
        return true;
    }


    getForm(step) {
        if (step === 1) {
            return <span>
                <h1>
                    Find your song genre
            </h1>
                <Button variant="warning" id="btnStart" onClick={this.nextStep}>Continue</Button>
            </span>;
        }
        else if (step === 2) {
            return <span>
                <h1>Upload File</h1>
                <input type="file" name="file" id="chooseFile" onChange={this.onChangeHandler} />
                {this.state.selectedFile != null ?
                    <Button variant="warning" id="findOut" onClick={this.nextStep}>Find Out</Button>
                    : null}
            </span>
        }
        else if (step === 3) {
            return <span>
                <h1 id="song">Result:</h1>
                <h1 id="fileName"><b>File Name:</b> {this.state.fileName}</h1>
                <h1 id="genre"><b>Song Genre:</b> {this.state.songGenre}</h1>
                <div>
                    {this.state.genre != null && this.state.songName != null ?
                        <Button variant="warning" id="tryAgain" onClick={this.nextStep}>Try again</Button>
                        : null}
                </div>
            </span>
        }
    }

    render() {
        return (
            <React.Fragment>
                <Header />
                <ToastContainer position={toast.POSITION.BOTTOM_RIGHT} />
                <div id="box">
                    {this.getForm(this.state.step)}
                </div>
                <Footer />
            </React.Fragment>
        );
    }
}

export default Home;