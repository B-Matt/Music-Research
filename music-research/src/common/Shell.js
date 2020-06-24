import React from "react";
import { inject } from "mobx-react";
import { RouterView } from "mobx-state-router";
import Home from "../components/Home";
import NotFoundPage from "../components/NotFound";
import Songs from "../components/Songs";
import Discover from "../components/Discover";

const viewMap = {
  home: <Home />,
  notFound: <NotFoundPage />,
  songs: <Songs />,
  discover: <Discover />,
};

export const Shell = inject("rootStore")(
  class extends React.Component {
    render() {
      const { rootStore } = this.props;
      const { routerStore } = rootStore;

      return <RouterView routerStore={routerStore} viewMap={viewMap} />;
    }
  }
);
