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
import Requirement from "./pages/Requirement";
import RequirementLayout from "./components/RequirementLayout";
import UseCases from "./pages/Requirement/UseCases";
import IndividualReqComponent from "./pages/Requirement/IndividualReqComponent";
import Invoker from "./pages/Invoker";
import { ReliabilityPrivateRoute } from "./reliability/ReliabilityPrivateRoute";
import ReliabilityLayout from "./reliability/components/ReliabilityLayout";
import ReliabilityHome from "./reliability/pages/ReliabilityHome";
import MonitoringDashboard from "./reliability/pages/MonitoringDasboard";
import ReliRun from "./reliability/pages/ReliRun";
import Holidays from "./capacity-planner/pages/Holidays";
import ReliTarget from "./reliability/pages/ReliTarget";
import GrowthTarget from "./reliability/pages/GrowthTarget";
import { DefectsPrivateRoute } from "./defects/DefectsPrivateRoute";
import DefectsHome from "./defects/pages/DefectsHome";
import AllDefects from "./defects/pages/AllDefects";
import DefectsLayout from "./defects/components/DefectsLayout";
import IndividualDefect from "./defects/pages/IndividualDefect";

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
              path={`/requirements/:orggroup`}
              element={<RequirementLayout page={<Requirement />} auth={true} />}
            />
            <Route
              path={`/requirements/:orggroup/:reqcatid`}
              element={<RequirementLayout page={<Requirement />} auth={true} />}
            />
            <Route
              path={`/requirements/use-cases`}
              element={<RequirementLayout page={<UseCases />} auth={true} />}
            />
            <Route
              path={`/requirement/:requirementidparam`}
              element={
                <RequirementLayout
                  page={<IndividualReqComponent />}
                  auth={true}
                />
              }
            />
            <Route
              path={`/invoker`}
              element={<Layout page={<Invoker />} auth={true} />}
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

            <Route path="/holidays" element={<Layout page={<Holidays />} />} />

            <Route path="/reliability" element={<ReliabilityPrivateRoute />}>
              <Route
                path="/reliability"
                element={
                  <ReliabilityLayout page={<ReliabilityHome />} auth={true} />
                }
              />
            </Route>
            <Route
              path="/reliability/monitoring"
              element={<ReliabilityPrivateRoute />}
            >
              <Route
                path="/reliability/monitoring"
                element={
                  <ReliabilityLayout
                    page={<MonitoringDashboard />}
                    auth={true}
                  />
                }
              />
            </Route>
            <Route
              path="/reliability/target/demonstration"
              element={<ReliabilityPrivateRoute />}
            >
              <Route
                path="/reliability/target/demonstration"
                element={
                  <ReliabilityLayout page={<ReliTarget />} auth={true} />
                }
              />
            </Route>
            <Route
              path="/reliability/target/growth"
              element={<ReliabilityPrivateRoute />}
            >
              <Route
                path="/reliability/target/growth"
                element={
                  <ReliabilityLayout page={<GrowthTarget />} auth={true} />
                }
              />
            </Route>
            <Route
              path="/reliability/monitoring/:relirunID"
              element={<ReliabilityPrivateRoute />}
            >
              <Route
                path="/reliability/monitoring/:relirunID"
                element={<ReliabilityLayout page={<ReliRun />} auth={true} />}
              />
            </Route>
            <Route path="/defects" element={<DefectsPrivateRoute />}>
              <Route
                path="/defects"
                element={<DefectsLayout page={<DefectsHome />} auth={true} />}
              />
            </Route>
            <Route
              path="/defects/all-defects"
              element={<DefectsPrivateRoute />}
            >
              <Route
                path="/defects/all-defects"
                element={<DefectsLayout page={<AllDefects />} auth={true} />}
              />
            </Route>
            <Route path="/defects/:defectID" element={<DefectsPrivateRoute />}>
              <Route
                path="/defects/:defectID"
                element={
                  <DefectsLayout page={<IndividualDefect />} auth={true} />
                }
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
