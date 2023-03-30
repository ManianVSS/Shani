import { AppShell } from "@mantine/core";
import React from "react";
import { theme } from "../../theme";
import { NavbarNested } from "../NavbarComponent";
import { useRecoilState } from "recoil";
import { sideBar } from "../../state/mode";
import Draggable from "react-draggable";
import { LogOutIcon, Menu, MenuIcon, Popover, Position } from "evergreen-ui";
import { Settings } from "@mui/icons-material";
import FloatingButton from "../FloatingButton";

const Layout = (props) => {
  const [sideBarState, setSideBarState] = useRecoilState(sideBar);
  return (
    <div>
      {sideBarState === "open" ? (
        <AppShell
          padding="md"
          navbar={<NavbarNested />}
          styles={(theme) => ({
            main: {
              backgroundColor:
                theme.colorScheme === "dark"
                  ? theme.colors.dark[8]
                  : theme.colors.gray[0],
            },
          })}
        >
          {props.page}
        </AppShell>
      ) : (
        <div>
          <Draggable>
            <Popover
              position={Position.BOTTOM_RIGHT}
              content={
                <Menu>
                  <Menu.Group>
                    <Menu.Item
                      icon={Settings}
                      onClick={() => {
                        setSideBarState("open");
                      }}
                    >
                      Open Sidebar
                    </Menu.Item>
                  </Menu.Group>
                  <Menu.Divider />
                  <Menu.Group>
                    <Menu.Item icon={LogOutIcon} intent="danger">
                      Logout
                    </Menu.Item>
                  </Menu.Group>
                </Menu>
              }
            >
              <div>
                <FloatingButton />
              </div>
            </Popover>
          </Draggable>
          {props.page}
        </div>
      )}
    </div>
  );
};

export default Layout;
