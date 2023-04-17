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
import { Button, Dropdown, Form } from "react-bootstrap";
import { Menu, PersonIcon, LogOutIcon } from "evergreen-ui";
import { useRecoilState, useRecoilValue } from "recoil";
import { colorScheme, sideBar } from "../../state/mode";
import DarkModeToggle from "react-dark-mode-toggle";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  AddHomeOutlined,
  AdminPanelSettings,
  Settings,
  ReduceCapacity
} from "@mui/icons-material";
import { axiosClient } from "../../hooks/api";
import { globalNavData } from "../../state/globalNavData";
import { allPagesData } from "../../state/allPagesData";
import "./style.css";

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
    borderBottom: `1px solid ${theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
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
    borderTop: `1px solid ${theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
      }`,
  },
}));

export function NavbarNested() {
  const navData = useRecoilValue(globalNavData);
  const { siteid, catalogid, categoryid, pageid } = useParams();

  let siteData: any[] = [];
  siteData = navData.filter((site) => {
    return site.id === parseInt(siteid ?? "0");
  });

  let catalogMenu: any[] = [];
  siteData[0]?.catalogs?.map((item) => {
    catalogMenu.push({
      id: item.id,
      name: item.name,
      link: "/site/" + siteid + "/catalog/" + item.id,
    });
  });

  let catalogData: any[] = [];
  catalogData = siteData[0]?.catalogs?.filter((catalog) => {
    return catalog.id === parseInt(catalogid ?? "0");
  });

  const navigate = useNavigate();
  const { classes } = useStyles();
  let data = catalogData ?? [{ label: "Home", icon: IconHome, link: "/" }];
  const links = data[0]?.categories?.map((item) => (
    <LinksGroup {...item} key={item.label} />
  ));
  const [mode, setMode] = useRecoilState(colorScheme);
  const [isDarkMode, setIsDarkMode] = useState(
    window.localStorage.getItem("testCenterTheme") === "dark"
  );
  const [sideBarState, setSideBarState] = useRecoilState(sideBar);

  const onChange = (event) => {
    const value = event.target.value;
    navigate(value);
  };

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

          <Form.Select
            aria-label=""
            onChange={onChange}
          // onClick={() => {
          //   navigate(0);
          // }}
          >
            {catalogMenu.map((item) => {
              return (
                <option
                  value={item.link}
                  selected={item.link === catalogData[0]?.link}
                >
                  {item.name}
                </option>
              );
            })}
          </Form.Select>

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
                    <Menu.Item
                      icon={ReduceCapacity}
                      style={{ margin: 0 }}
                      onClick={() => {
                        navigate(`/capacity-planner/`)
                      }}
                    >
                      Capacity Planner
                    </Menu.Item>
                  </Menu.Group>
                  <Menu.Group>
                    <Menu.Item
                      icon={AdminPanelSettings}
                      style={{ margin: 0 }}
                      onClick={() => {
                        window.open(
                          "http://" + window.location.host + "/admin/",
                          "_blank"
                        );
                      }}
                    >
                      Admin
                    </Menu.Item>
                  </Menu.Group>
                  <Menu.Group>
                    <Menu.Item
                      icon={AddHomeOutlined}
                      style={{ margin: 0 }}
                      onClick={() => {
                        window.open(
                          "http://" + window.location.host + "/swagger/",
                          "_blank"
                        );
                      }}
                    >
                      Swagger
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
                  {/* <Menu.Group>
                    <Menu.Item
                      icon={LogOutIcon}
                      intent="danger"
                      style={{ margin: 0 }}
                    >
                      Logout
                    </Menu.Item>
                  </Menu.Group> */}
                </Menu>
              </Popover.Body>
            </Popover>
          }
        >
          <div>
            <UserButton image="" name="User Name" email="user@something.com" />
          </div>
        </OverlayTrigger>
      </Navbar.Section>
    </Navbar>
  );
}
