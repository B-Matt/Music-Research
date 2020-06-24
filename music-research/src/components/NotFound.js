import React from "react";
import NavigationBar from "./NavigationBar";

export default class NotFoundPage extends React.Component {
  render() {
    return (
      <div id="box">
        <header>
          <NavigationBar />
          <h1>Page Not Found</h1>
        </header>
      </div>
    );
  }
}
