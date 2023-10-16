import { AppShell } from "@mantine/core";
import React from "react";
import { NavbarNested } from "../NavbarComponent";
import { useRecoilState } from "recoil";
import { sideBar } from "../../state/mode";
import Draggable from "react-draggable";
import { Menu, Popover, Position } from "evergreen-ui";
import { Settings } from "@mui/icons-material";
import FloatingButton from "../FloatingButton";
// import { authState } from "../../state/authData";

const Layout = (props) => {
  const [sideBarState, setSideBarState] = useRecoilState(sideBar);
  // const [auth, setAuth] = useRecoilState(authState);
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
                </Menu>
              }
            >
              <div>
                <FloatingButton style={{ zIndex: 1 }} />
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
