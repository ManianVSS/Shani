import { AppShell } from "@mantine/core";
import React from "react";
import { NavbarRequirementModule } from "../../pages/Requirement/NavbarRequirementModule";

const requirementLayout = (props) => {
  return (
    <div>
      {props.auth ? (
        <AppShell
          padding="md"
          navbar={<NavbarRequirementModule />}
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

export default requirementLayout;
