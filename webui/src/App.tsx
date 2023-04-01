import { MantineProvider } from "@mantine/core";
import { RecoilRoot, useRecoilState, useRecoilValue } from "recoil";
// import { theme } from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";

import { MantineThemeOverride, ColorScheme } from "@mantine/core";
import { colorScheme } from "./state/mode";
import Category from "./pages/Category";
import "@tremor/react/dist/esm/tremor.css";
import Dashboard from "./pages/Dashboard";
import Documentation from "./pages/Documentation";
import { globalNavData } from "./state/globalNavData";
import { allPagesData } from "./state/allPagesData";
import { axiosClient } from "./hooks/api";
import { IconFileAnalytics, IconHome, TablerIcon } from "@tabler/icons";
import { useEffect } from "react";
import NotFound from "./pages/NotFound";

interface customLinks {
  label: string;
  link: string;
}

export default function App() {
  const mode = useRecoilValue(colorScheme);

  const [nav, setNav] = useRecoilState(globalNavData);
  const [allPages, setAllPages] = useRecoilState(allPagesData);
  function getItemsFromArray(items): customLinks[] {
    let children: customLinks[] = [];
    items.map((item) => {
      children.push({
        label: item.name,
        link: item.name.replace(" ", "_"),
      });
    });
    return children;
  }
  const getNavigationData = () => {
    let navData: {
      label: string;
      icon: TablerIcon;
      links: { label: string; link: string }[];
      link: string;
    }[] = [];
    axiosClient.get("site_details").then((respose) => {
      respose.data.map((item) => {
        navData.push({
          label: item["name"],
          icon: item["name"] === "Home" ? IconHome : IconFileAnalytics,
          links:
            item["pages"].length === 0 ? [] : getItemsFromArray(item["pages"]),
          link: "/site/" + item["name"],
        });
      });
      setAllPages(respose.data);
      setNav(navData);
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
    <MantineProvider theme={darkTheme} withGlobalStyles withNormalizeCSS>
      <Router>
        <Routes>
          <Route path="/" element={<Layout page={<Home />} />} />
          <Route
            path={`/site/:categoryName`}
            element={<Layout page={<Category />} />}
          />
          <Route path="/dashboard" element={<Layout page={<Dashboard />} />} />
          <Route
            path="/documentation"
            element={<Layout page={<Documentation />} />}
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    </MantineProvider>
  );
}
