import React from 'react';
import { Navbar } from 'react-bootstrap';
import Background from '../images/imgonlin.png'
import '../styles/header.css'

class Header extends React.Component {
  render() {
    return (
      <Navbar bg="navbar navbar-dark dark" expand="lg">
        <Navbar.Brand href="#home">
          <img src={Background} height="105" alt="Music Research Logo" />
        </Navbar.Brand>
      </Navbar>
    );
  }
}

export default Header;