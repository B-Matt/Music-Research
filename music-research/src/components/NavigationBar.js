import React from "react";
import "../styles/header.css";
import { Navbar, Nav } from "react-bootstrap";
import logo from "../images/logo.png";

class NavigationBar extends React.Component {
  render() {
    return (
      <nav>
        <Navbar collapseOnSelect sticky="top" expand="md">
          <Navbar.Brand href="/">
            <img src={logo} alt="React Bootstrap logo" className="logo" />
          </Navbar.Brand>
          <Navbar.Toggle
            aria-controls="responsive-navbar-nav"
            id="btnToggle"
            className="ml-auto"
          />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link className="nav-item" href="/">
                Home
              </Nav.Link>
              <Nav.Link className="nav-item" href="/songs">
                Songs
              </Nav.Link>
              <Nav.Link className="nav-item" href="/discover">
                Discover
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </nav>
    );
  }
}

export default NavigationBar;
