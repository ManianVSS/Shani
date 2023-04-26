import React, { useEffect } from "react";
import {
  Popover,
  Menu,
  Position,
  PersonIcon,
  LogOutIcon,
  Button,
} from "evergreen-ui";
import { useRecoilState, useRecoilValue } from "recoil";
import { globalNavData } from "../../state/globalNavData";
import { useNavigate } from "react-router-dom";
import { axiosClient } from "../../hooks/api";
import { IconFileAnalytics, IconHome } from "@tabler/icons";
import { colorScheme } from "../../state/mode";

const Home = () => {
  const navigateToFirstItem = () => {
    let navData = [];
    axiosClient.get("site_details").then((respose) => {
      // respose.data[0].catalogs.map((item) => {
      //   navData.push({
      //     label: item["name"],
      //     icon: item["name"] === "Home" ? IconHome : IconFileAnalytics,
      //     link: "/site/" + item["id"],
      //   });
      // });
      navigate(
        "/site/" +
          respose.data[0]?.id +
          "/catalog/" +
          respose.data[0]?.catalogs[0]?.id
      );
    });
  };

  const navigate = useNavigate();
  useEffect(() => {
    navigateToFirstItem();
  }, []);
  return <div>Home</div>;
};

export default Home;
