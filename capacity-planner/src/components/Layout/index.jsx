import React, { useContext } from "react";
import { AppShell } from "@mantine/core";
import { NavbarSimpleColored } from "../NavbarSimpleColored";
import { theme } from "../../theme";

const Layout = (props) => {
  return (
    <div>
      {props.auth ? (
        <AppShell
          padding="md"
          navbar={<NavbarSimpleColored />}
          // header={<Header height={60} p="xs">{/* Header content */}</Header>}
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
        props.page
      )}
    </div>
  );
};

export default Layout;
