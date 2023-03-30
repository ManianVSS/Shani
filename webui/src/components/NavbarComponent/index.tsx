import { Navbar, Group, Code, ScrollArea, createStyles } from "@mantine/core";
import {
  IconNotes,
  IconCalendarStats,
  IconGauge,
  IconPresentationAnalytics,
  IconFileAnalytics,
  IconAdjustments,
  IconLock,
  IconHome,
  TablerIcon,
} from "@tabler/icons";

import { LinksGroup } from "./NavbarLinksGroup/NavbarLinksGroup";
import { UserButton } from "./UserButton";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Popover from "react-bootstrap/Popover";
import { Button } from "react-bootstrap";
import { Menu, PersonIcon, LogOutIcon } from "evergreen-ui";
import { useRecoilState } from "recoil";
import { colorScheme, sideBar } from "../../state/mode";
import DarkModeToggle from "react-dark-mode-toggle";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Settings } from "@mui/icons-material";
import { axiosClient } from "../../hooks/api";
import { globalNavData } from "../../state/globalNavData";
import { allPagesData } from "../../state/allPagesData";

const useStyles = createStyles((theme) => ({
  navbar: {
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.white,
    paddingBottom: 0,
  },

  header: {
    padding: theme.spacing.md,
    paddingTop: 0,
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    borderBottom: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
  },

  links: {
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
  },

  linksInner: {
    paddingTop: theme.spacing.xl,
    paddingBottom: theme.spacing.xl,
  },

  footer: {
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
    borderTop: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
  },
}));

export function NavbarNested() {
  const [nav, setNav] = useRecoilState(globalNavData);
  const [allPages, setAllPages] = useRecoilState(allPagesData);
  const getNavigationData = () => {
    let navData: { label: string; icon: TablerIcon; link: string }[] = [];
    axiosClient.get("site_details").then((respose) => {
      respose.data.map((item) => {
        navData.push({
          label: item["name"],
          icon: item["name"] === "Home" ? IconHome : IconFileAnalytics,
          link: item["name"] === "Home" ? "/" : "/category/" + item["name"],
        });
      });
      setAllPages(respose.data);
      setNav(navData);
    });
  };

  const navigate = useNavigate();
  const { classes } = useStyles();
  // let mockdata = [
  //   { label: "Home", icon: IconHome, link: "/" },
  //   {
  //     label: "Category 1",
  //     icon: IconNotes,
  //     initiallyOpened: false,
  //     links: [
  //       { label: "Sub Category 1", link: "/category2" },
  //       { label: "Sub Category 2", link: "/" },
  //       { label: "Sub Category 3", link: "/" },
  //       { label: "Sub Category 4", link: "/" },
  //     ],
  //     link: "/",
  //   },
  //   {
  //     label: "Category 3",
  //     icon: IconCalendarStats,
  //     links: [
  //       { label: "Upcoming releases", link: "/" },
  //       { label: "Previous releases", link: "/" },
  //       { label: "Releases schedule", link: "/" },
  //     ],
  //     link: "/",
  //   },
  //   { label: "Reports", icon: IconPresentationAnalytics, link: "/dashboard" },
  //   { label: "Documentation", icon: IconFileAnalytics, link: "/documentation" },
  //   { label: "Settings", icon: IconAdjustments, link: "/" },
  //   {
  //     label: "Security",
  //     icon: IconLock,
  //     links: [
  //       { label: "Enable 2FA", link: "/" },
  //       //   { label: "Change password", link: "/" },
  //       { label: "Recovery codes", link: "/" },
  //     ],
  //     link: "/",
  //   },
  // ];

  const links = nav.map((item) => <LinksGroup {...item} key={item.label} />);
  const [mode, setMode] = useRecoilState(colorScheme);
  const [isDarkMode, setIsDarkMode] = useState(
    window.localStorage.getItem("testCenterTheme") === "dark"
  );
  const [sideBarState, setSideBarState] = useRecoilState(sideBar);

  useEffect(() => {
    getNavigationData();
  }, []);
  return (
    <Navbar
      // height={800}
      width={{ sm: 300 }}
      p="md"
      className={classes.navbar}
    >
      <Navbar.Section className={classes.header}>
        <Group position="apart">
          {/* <Logo width={120} /> */}
          <p style={{ fontSize: "20px" }}>
            <b>Dashboard</b>
          </p>
          <Code sx={{ fontWeight: 700 }}>v1.0.0</Code>
          <DarkModeToggle
            onChange={() => {
              setIsDarkMode((curr) => !curr);
              if (mode === "light") {
                setMode("dark");
                window.localStorage.setItem("testCenterTheme", "dark");
              } else {
                setMode("light");
                window.localStorage.setItem("testCenterTheme", "light");
              }
            }}
            checked={isDarkMode}
            size={40}
          />
        </Group>
      </Navbar.Section>

      <Navbar.Section grow className={classes.links} component={ScrollArea}>
        <div className={classes.linksInner}>{links}</div>
      </Navbar.Section>

      <Navbar.Section className={classes.footer}>
        <OverlayTrigger
          trigger="click"
          key={"top"}
          placement={"top"}
          overlay={
            <Popover id={`popover-positioned-${"top"}`}>
              <Popover.Body style={{ margin: 0, padding: 0 }}>
                <Menu>
                  <Menu.Group>
                    <Menu.Item icon={PersonIcon} style={{ margin: 0 }}>
                      Profile
                    </Menu.Item>
                  </Menu.Group>
                  <Menu.Group>
                    <Menu.Item
                      icon={Settings}
                      style={{ margin: 0 }}
                      onClick={() => {
                        setSideBarState("closed");
                      }}
                    >
                      Hide Sidebar
                    </Menu.Item>
                  </Menu.Group>
                  <Menu.Divider />
                  <Menu.Group>
                    <Menu.Item
                      icon={LogOutIcon}
                      intent="danger"
                      style={{ margin: 0 }}
                    >
                      Logout
                    </Menu.Item>
                  </Menu.Group>
                </Menu>
              </Popover.Body>
            </Popover>
          }
        >
          <div>
            <UserButton
              image=""
              name="Aditya Sheshagiri"
              email="aditya@something.com"
            />
          </div>
        </OverlayTrigger>
      </Navbar.Section>
    </Navbar>
  );
}
