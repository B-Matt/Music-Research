import React from "react";
import NavigationBar from "../components/NavigationBar";
import Footer from "../components/Footer";
import "react-toastify/dist/ReactToastify.css";
import "../styles/home.css";
import country from "../images/country.jfif";
import blues from "../images/blues.jpg";
import jazz from "../images/jazz.jpg";
import techno from "../images/techno.jfif";
import rock from "../images/rock.jfif";
import metal from "../images/metal.jfif";
import pop from "../images/pop.png";
import reggae from "../images/reggae.jfif";
import classical from "../images/classical.jfif";
import hiphop from "../images/hiphop.jfif";
import disco from "../images/disco.jpg";
import dance from "../images/dance.jfif";
import trance from "../images/trance.jpg";

class Home extends React.Component {
  render() {
    return (
      <React.Fragment>
        <header>
          <NavigationBar />
          <h1>Music Research</h1>
          <h2 className="saving">
            Discover your music genre<span className="dot">.</span>
            <span className="dot">.</span>
            <span className="dot">.</span>
          </h2>
          <svg className="arrows">
            <path className="a1" d="M0 0 L30 32 L60 0"></path>
            <path className="a2" d="M0 20 L30 52 L60 20"></path>
            <path className="a3" d="M0 40 L30 72 L60 40"></path>
            <path className="a4" d="M0 60 L30 92 L60 60"></path>
          </svg>
        </header>
        <h2 className="new-section">Genres</h2>
        <div className="py-5 ">
          <div className="container">
            <div className="row">
              <div className="card">
                <img src={country} alt="Country img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Country</h4>
                </div>
              </div>
              <div className="card">
                <img src={blues} alt="Blues img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Blues</h4>
                </div>
              </div>
              <div className="card">
                <img src={jazz} alt="Jazz img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Jazz</h4>
                </div>
              </div>
              <div className="card">
                <img src={techno} alt="Techno img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Techno</h4>
                </div>
              </div>
              <div className="card">
                <div className="card-block text-center">
                  <img src={rock} alt="Rock img" />
                  <h4 className="card-title">Rock</h4>
                </div>
              </div>
              <div className="card">
                <img src={metal} alt="Metal img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Metal</h4>
                </div>
              </div>
              <div className="card">
                <img src={pop} alt="Pop img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Pop</h4>
                </div>
              </div>
              <div className="card">
                <img src={reggae} alt="Reggae img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Reggae</h4>
                </div>
              </div>
              <div className="card">
                <img src={classical} alt="Classical img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Classical</h4>
                </div>
              </div>
              <div className="card">
                <img src={hiphop} alt="HipHop img" />
                <div className="card-block text-center">
                  <h4 className="card-title">HipHop</h4>
                </div>
              </div>
              <div className="card">
                <img src={disco} alt="Disco img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Disco</h4>
                </div>
              </div>
              <div className="card">
                <img src={dance} alt="Dance img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Dance</h4>
                </div>
              </div>
              <div className="card">
                <img src={trance} alt="Trance img" />
                <div className="card-block text-center">
                  <h4 className="card-title">Trance</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </React.Fragment>
    );
  }
}

export default Home;
