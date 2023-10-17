import { MantineProvider } from "@mantine/core";
import { useRecoilState, useRecoilValue } from "recoil";
// import { theme } from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";

import { MantineThemeOverride } from "@mantine/core";
import { colorScheme } from "./state/mode";
import Category from "./pages/Category";
import "@tremor/react/dist/esm/tremor.css";

import { globalNavData } from "./state/globalNavData";
import { allPagesData } from "./state/allPagesData";
import { axiosClient } from "./hooks/api";
import { IconFileAnalytics, IconHome } from "@tabler/icons";
import { useEffect } from "react";
import NotFound from "./pages/NotFound";
import AlertTemplate from "./capacity-planner/components/AlertTemplate";
import { transitions, positions, Provider as AlertProvider } from "react-alert";
import CapacityLayout from "./capacity-planner/components/CapacityLayout";
import Capacity from "./capacity-planner/pages/Capacity";
import EngineerAvailability from "./capacity-planner/pages/EngineerAvailability";
import Leaves from "./capacity-planner/pages/Leaves";
import Login from "./pages/Login";
import { CapacityPrivateRoute } from "./capacity-planner/CapacityPrivateRoute";
import CapacityHome from "./capacity-planner/pages/CapacityHome";
import Profile from "./pages/Profile";

interface customLinks {
  label: string;
  link: string;
}
const options = {
  // you can also just use 'bottom center'
  position: positions.TOP_RIGHT,
  timeout: 5000,
  offset: "30px",
  // you can also just use 'scale'
  transition: transitions.SCALE,
};

export default function App() {
  const mode = useRecoilValue(colorScheme);

  const [nav, setNav] = useRecoilState(globalNavData);
  const [allPages, setAllPages] = useRecoilState(allPagesData);
  function getItemsFromArray(
    items,
    siteID,
    catalogID,
    categoryID
  ): customLinks[] {
    let children: customLinks[] = [];
    items.map((item) => {
      children.push({
        label: item.name,
        link:
          "/site/" +
          siteID +
          "/catalog/" +
          catalogID +
          "/category/" +
          categoryID +
          "/page/" +
          item["id"],
      });
    });
    return children;
  }

  function getAllCategories(items, siteID, catalogID): any[] {
    let children: any[] = [];
    items.map((item) => {
      children.push({
        label: item["name"],
        icon: item["name"] === "Home" ? IconHome : IconFileAnalytics,
        links:
          item["pages"].length === 0
            ? []
            : getItemsFromArray(item["pages"], siteID, catalogID, item["id"]),
        link:
          "/site/" +
          siteID +
          "/catalog/" +
          catalogID +
          "/category/" +
          item["id"],
      });
    });
    return children;
  }

  function getAllCatalogs(items, siteID): any[] {
    let children: any[] = [];
    items.map((item) => {
      children.push({
        id: item.id,
        name: item.name,
        link: "/site/" + siteID + "/catalog/" + item["id"],
        categories: getAllCategories(item["categories"], siteID, item.id),
      });
    });
    return children;
  }

  const getNavigationData = () => {
    let data: any[] = [];
    axiosClient.get("site_details").then((respose) => {
      respose.data.map((item) => {
        data.push({
          id: item["id"],
          name: item["name"],
          catalogs: getAllCatalogs(item["catalogs"], item["id"]),
        });
      });
      setAllPages(respose.data);
      setNav(data);
    });
  };

  if (mode === "dark") {
    var darkTheme: MantineThemeOverride = {
      colorScheme: "dark",
    };
  } else {
    var darkTheme: MantineThemeOverride = {
      colorScheme: "light",
    };
  }

  useEffect(() => {
    getNavigationData();
  }, []);
  return (
    <AlertProvider template={AlertTemplate} {...options}>
      <MantineProvider theme={darkTheme} withGlobalStyles withNormalizeCSS>
        <Router>
          <Routes>
            <Route path="/" element={<Layout page={<Home />} />} />
            <Route
              path={`/site/:siteid/catalog/:catalogid`}
              element={<Layout page={<Category />} />}
            />
            <Route
              path={`/site/:siteid/catalog/:catalogid/category/:categoryid`}
              element={<Layout page={<Category />} />}
            />
            <Route
              path={`/site/:siteid/catalog/:catalogid/category/:categoryid/page/:pageid`}
              element={<Layout page={<Category />} />}
            />
            <Route
              path={`/site/profile`}
              element={<Layout page={<Profile />} />}
            />
            <Route
              path="/login"
              element={<CapacityLayout page={<Login />} auth={false} />}
            />

            {/* <Route path="/dashboard" element={<Layout page={<Dashboard />} />} />
          <Route
            path="/documentation"
            element={<Layout page={<Documentation />} />}
          /> */}

            <Route path="/capacity-planner" element={<CapacityPrivateRoute />}>
              <Route
                path="/capacity-planner"
                element={<CapacityLayout page={<CapacityHome />} auth={true} />}
              />
            </Route>
            <Route
              path="/capacity-planner/capacity"
              element={<CapacityPrivateRoute />}
            >
              <Route
                path="/capacity-planner/capacity"
                element={<CapacityLayout page={<Capacity />} auth={true} />}
              />
            </Route>
            <Route
              path="/capacity-planner/engineer-availability"
              element={<CapacityPrivateRoute />}
            >
              <Route
                path="/capacity-planner/engineer-availability"
                element={
                  <CapacityLayout page={<EngineerAvailability />} auth={true} />
                }
              />
            </Route>
            <Route
              path="/capacity-planner/leaves"
              element={<CapacityPrivateRoute />}
            >
              <Route
                path="/capacity-planner/leaves"
                element={<CapacityLayout page={<Leaves />} auth={true} />}
              />
            </Route>
            {/* <Route
              path="/capacity-planner/login"
              element={<CapacityLayout page={<Login />} auth={false} />}
            /> */}
            <Route path="*" element={<NotFound />} />
            <Route path="/notfound" element={<NotFound />} />
          </Routes>
        </Router>
      </MantineProvider>
    </AlertProvider>
  );
}
