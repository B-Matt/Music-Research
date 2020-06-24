import React from "react";
import HttpClient from "../common/HttpClient";
import "../styles/songs.css";
import NavigationBar from "./NavigationBar";
import Footer from "./Footer";

export default class Songs extends React.Component {
  constructor(props) {
    super(props);
    this.httpClient = new HttpClient();
    this.getSongs = this.getSongs.bind(this);
    this.getGenres = this.getGenres.bind(this);
    this.put = this.put.bind(this);
    this.remove = this.remove.bind(this);
    this.sort = this.sort.bind(this);
    this.state = {
      data: [],
      song: { Genre: "", Id: "", Name: "" },
    };
  }

  componentDidMount(){
    this.getSongs();
  }

  async getSongs() {
    try {
      this.httpClient.getSongs().then((response) => {
        this.setState({
          data: [...response],
        });
      });
    } catch (error) {
      console.log(error);
    }
  }

  async getGenres() {
    try {
      this.httpClient.getGenres().then((response) => {
        this.setState({
          genres: response,
        });
      });
    } catch (error) {
      console.log(error);
    }
  }

  setData(item) {
    this.setState({ song: item });
  }

  put(item) {
    try {
      this.httpClient.put(item).then((response) => {
        this.getSongs();
      });
    } catch (error) {
      console.log(error);
    }
  }

  changeName(e) {
    this.setState({
      song: {
        ...this.state.song,
        Name: e.target.value,
      },
    });
  }

  remove(id) {
    try {
      this.httpClient.remove(id).then((response) => {
        this.getSongs();
      });
    } catch (error) {
      console.log(error);
    }
  }

  sort(sortName) {
    const sorted = [...this.state.data].sort(
      (a, b) => b[sortName] - a[sortName]
    );

    this.setState({
      data: sorted,
    });
  }

  render() {
    return (
      <React.Fragment>
        <div className="songs">
          <header className="navBar">
            <NavigationBar />
          </header>
          <div className="containerTable">
            <div className="row col-md-12">
              <div className="col-md-12">
                <h4>Songs</h4>
                <table
                  id="mytable"
                  className="table table-bordred table-striped"
                >
                  <thead>
                    <tr>
                      <th onClick={() => this.sort("Name")}>Song Name</th>
                      <th onClick={() => this.sort("Genre")}>Genre</th>
                      <th>Edit</th>
                      <th>Delete</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(this.state.data.length > 0) ? (
                      this.state.data.map((item, i) => (
                        <tr key={i}>
                          <td>{item.Name}</td>
                          <td>{item.Genre}</td>
                          <td>
                            <p
                              data-placement="top"
                              onClick={() => this.setData(item)}
                              data-toggle="tooltip"
                              title="Edit"
                            >
                              <button
                                className="btn btn-primary btn-xs"
                                data-title="Edit"
                                data-toggle="modal"
                                data-target="#edit"
                              >
                                <span className="glyphicon glyphicon-pencil"></span>
                              </button>
                            </p>
                          </td>
                          <td>
                            <p
                              data-placement="top"
                              onClick={() => this.setData(item)}
                              data-toggle="tooltip"
                              title="Delete"
                            >
                              <button
                                className="btn btn-danger btn-xs"
                                data-title="Delete"
                                data-toggle="modal"
                                data-target="#delete"
                              >
                                <span className="glyphicon glyphicon-trash"></span>
                              </button>
                            </p>
                          </td>
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td>Loading</td>
                        <td></td>
                        <td></td>
                        <td></td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div
            className="modal fade"
            id="edit"
            tabIndex="-1"
            role="dialog"
            aria-labelledby="edit"
            aria-hidden="true"
          >
            <div className="modal-dialog">
              <div className="modal-content">
                <div className="modal-header">
                  <button
                    type="button"
                    className="close"
                    data-dismiss="modal"
                    aria-hidden="true"
                  >
                    <span
                      className="glyphicon glyphicon-remove"
                      aria-hidden="true"
                    ></span>
                  </button>
                  <h4 className="modalTitle">Edit</h4>
                </div>
                <div className="modal-body">
                  <div className="form-group">
                    <label>Song name:</label>
                    <br />
                    <input
                      className="form-control"
                      type="text"
                      placeholder="Song Name"
                      value={this.state.song.Name}
                      onChange={this.changeName.bind(this)}
                    ></input>
                  </div>
                </div>
                <div className="modal-footer ">
                  <button
                    type="button"
                    className="btn btn-warning btn-lg"
                    onClick={() => this.put(this.state.song)}
                    data-dismiss="modal"
                  >
                    <span className="glyphicon glyphicon-ok-sign"></span> Update
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div
            className="modal fade"
            id="delete"
            tabIndex="-1"
            role="dialog"
            aria-labelledby="edit"
            aria-hidden="true"
          >
            <div className="modal-dialog">
              <div className="modal-content">
                <div className="modal-header">
                  <button
                    type="button"
                    className="close"
                    data-dismiss="modal"
                    aria-hidden="true"
                  >
                    <span
                      className="glyphicon glyphicon-remove"
                      aria-hidden="true"
                    ></span>
                  </button>
                  <h4 className="modal-title custom_align" id="Heading">
                    Delete
                  </h4>
                </div>
                <div className="modal-body">
                  <div className="alert alert-danger">
                    <span className="glyphicon glyphicon-warning-sign"></span>{" "}
                    Are you sure you want to delete this song?
                  </div>
                </div>
                <div className="modal-footer ">
                  <button
                    type="button"
                    className="btn btn-success"
                    data-dismiss="modal"
                    onClick={() => this.remove(this.state.song.Id)}
                  >
                    <span className="glyphicon glyphicon-ok-sign"></span> Yes
                  </button>
                  <button
                    type="button"
                    className="btn btn-default"
                    data-dismiss="modal"
                  >
                    <span className="glyphicon glyphicon-remove"></span> No
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div id="footer">
            <Footer />
          </div>
        </div>
      </React.Fragment>
    );
  }
}
