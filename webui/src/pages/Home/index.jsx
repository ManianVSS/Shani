import React, { useEffect } from "react";
import {
  Popover,
  Menu,
  Position,
  PersonIcon,
  LogOutIcon,
  Button,
} from "evergreen-ui";
import { useRecoilValue } from "recoil";
import { globalNavData } from "../../state/globalNavData";
import { useNavigate } from "react-router-dom";
import { axiosClient } from "../../hooks/api";
import { IconFileAnalytics, IconHome } from "@tabler/icons";

const Home = () => {
  const navigateToFirstItem = () => {
    let navData = [];
    axiosClient.get("site_details").then((respose) => {
      respose.data.map((item) => {
        navData.push({
          label: item["name"],
          icon: item["name"] === "Home" ? IconHome : IconFileAnalytics,
          link: "/site/" + item["name"],
        });
      });
      navigate(navData[0].link);
      // setAllPages(respose.data);
      // setNav(navData);
    });
  };

  const navigate = useNavigate();
  useEffect(() => {
    navigateToFirstItem();
  }, []);
  return <div>Home</div>;
};

export default Home;
