import React from "react";
import "../styles/discover.css";
import NavigationBar from "./NavigationBar";
import Footer from "./Footer";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import HttpClient from "../common/HttpClient";
import { ToastContainer, toast } from "react-toastify";

const createUuid = require("uuid/v1");

export default class Discover extends React.Component {
  constructor(props) {
    super(props);
    this.httpClient = new HttpClient();
    this.state = {
      selectedFile: null,
      loaded: 0,
      genre: "",
      fileName: "",
      setShow: false,
    };

    this.onChangeHandler = this.onChangeHandler.bind(this);
    this.uploadSong = this.uploadSong.bind(this);
    this.postSong = this.postSong.bind(this);
    this.uuidv1 = this.uuidv1.bind(this);
  }

  uuidv1() {
    return createUuid();
  }

  async uploadSong() {
    try {
      this.setState({
        enableBtn: null,
      });
      const uuid = this.uuidv1();
      this.httpClient.upload(this.state.selectedFile, uuid).then((response) => {
        if (response) {
          this.httpClient.findGenre(uuid).then((response) => {
            if (response) {
              toast.success("Upload song on Server successful!", {
                duration: 2000,
              });
              this.handleShow();
              this.setState({
                genre: response,
                selectedFile: null,
                fileName: "",
                enableBtn: false,
              });
              this.postSong(uuid, this.state.fileName, response);
            } else {
              toast.error("Upload song on Server failed!", {
                duration: 2000,
              });
            }
          });
        } else toast.error("Upload song on Server failed!", { duration: 2000 });

        this.setState({
          enableBtn: true,
        });
      });
    } catch (error) {
      console.log(error);
      this.setState({
        enableBtn: true,
      });
    }
  }

  onChangeHandler = (event) => {
    var file = event.target.files[0];
    if (this.checkFileType(event) && this.checkFileSize(event)) {
      this.setState({
        selectedFile: file,
        fileName: file.name,
        enableBtn: true,
      });
    } else {
      this.setState({
        selectedFile: null,
        fileName: "",
        enableBtn: null,
      });
    }
  };

  checkFileType = (event) => {
    let files = event.target.files;
    let err = "";
    const types = ["audio/mp3", "audio/mpeg"];
    for (var x = 0; x < files.length; x++) {
      if (types.every((type) => files[x].type !== type)) {
        err += files[x].type + " is not a supported format\n";
      }
    }

    if (err !== "") {
      event.target.value = null;

      toast.error("Wrong file format, please try with .MP3", {
        hideProgressBar: true,
        position: "bottom-right",
        closeOnClick: true,
        autoClose: 4000,
      });
      return false;
    }
    return true;
  };

  checkFileSize = (event) => {
    let files = event.target.files;
    let size = 30000000;
    let err = "";
    for (var x = 0; x < files.length; x++) {
      if (files[x].size > size) {
        err += files[x].type + " is too large, please pick a smaller file\n";
      }
    }
    if (err !== "") {
      event.target.value = null;
      toast.error("File is too large, please pick a smaller file (MAX 30MB)", {
        hideProgressBar: true,
        position: "bottom-right",
        closeOnClick: true,
        autoClose: 4000,
      });
      return false;
    }
    return true;
  };

  handleShow = () => {
    this.setState({
      show: true,
    });
  };

  handleClose = () => {
    this.setState({
      show: false,
    });
  };

  postSong = (id, songName, genre) => {
    this.httpClient.getGenre(genre).then((response) => {
      this.httpClient
        .postSong({ Id: id, Name: songName, GenreId: response.Id })
        .then((response) => {
          if (!response.ok) {
            toast.error("Post song on server failed!", { duration: 2000 });
          }
        });
    });
  };

  render() {
    return (
      <React.Fragment>
        <div className="songs">
          <header className="navBar">
            <NavigationBar />
          </header>
          <div id="uploadContainer">
            <h1 id="title">Upload File</h1>
            <div id="input">
              <input
                type="file"
                name="file"
                id="inputFile"
                onChange={this.onChangeHandler}
              />
            </div>
            <div id="findOut">
              <Button
                variant="info"
                id="btnFind"
                disabled={!this.state.enableBtn}
                onClick={this.uploadSong}
              >
                Find out
              </Button>
            </div>
          </div>
          <ToastContainer position={toast.POSITION.BOTTOM_RIGHT} />
          <Modal
            id="modal"
            show={this.state.show}
            onHide={this.handleClose}
            backdrop="static"
            keyboard={false}
            animation={true}
          >
            <Modal.Header>
              <Modal.Title id="songTitle">Song genre</Modal.Title>
            </Modal.Header>
            <Modal.Body id="genre">{this.state.genre}</Modal.Body>
            <Modal.Footer>
              <Button variant="outline-info" onClick={this.handleClose}>
                Close
              </Button>
            </Modal.Footer>
          </Modal>
          <div id="footer">
            <Footer />
          </div>
        </div>
      </React.Fragment>
    );
  }
}
