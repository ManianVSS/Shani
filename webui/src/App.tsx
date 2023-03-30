import { MantineProvider } from "@mantine/core";
import { RecoilRoot, useRecoilValue } from "recoil";
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

export default function App() {
  const mode = useRecoilValue(colorScheme);

  if (mode === "dark") {
    var darkTheme: MantineThemeOverride = {
      colorScheme: "dark",
    };
  } else {
    var darkTheme: MantineThemeOverride = {
      colorScheme: "light",
    };
  }
  const navData = useRecoilValue(globalNavData);
  return (
    <MantineProvider theme={darkTheme} withGlobalStyles withNormalizeCSS>
      <Router>
        <Routes>
          <Route path="/" element={<Layout page={<Home />} />} />
          <Route
            path={`/category/:categoryName`}
            element={<Layout page={<Category />} />}
          />
          <Route path="/dashboard" element={<Layout page={<Dashboard />} />} />
          <Route
            path="/documentation"
            element={<Layout page={<Documentation />} />}
          />
        </Routes>
      </Router>
    </MantineProvider>
  );
}
